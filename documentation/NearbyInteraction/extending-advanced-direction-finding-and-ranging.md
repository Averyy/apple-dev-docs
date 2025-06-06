# Extending advanced direction finding and ranging

**Framework**: Nearbyinteraction

Extend your app’s direction finding capabilities with data from Ultra Wideband devices.

#### Overview

Extended distance measurement (EDM) is a ranging capability available between devices with second generation Ultra Wideband (UWB) chips. EDM enables measuring precise distance between two Apple devices using ultra-wideband technology at significantly farther distances than was possible with the first generation UWB chip. In iOS 17 and watchOS 10 and later, EDM is available through the Nearby Interaction framework. This article describes the tradeoffs involved in using EDM and getting the best ranging performance for your app.

##### Detect Devices and Their Capabilities

A new UWB communication protocol enables the EDM capabilities in second generation UWB chips. To use this new measurement technology, both sides have to have the second generation chip, this includes iPhone 15, Apple Watch Series 9, Apple Watch Ultra 2, and later.

Devices with the second generation UWB chip are backwards compatible with the ranging technologies available on the first generation UWB chip. Second generation UWB chip-equipped devices can communicate with first generation devices and Made for iPhone (MFI)-certified third-party chipsets. However, when communicating with first generation devices, second generation devices operate at the performance available on the first generation chip. This article refers to Nearby Interaction peer sessions that don’t have extended distance measurement enabled as “legacy” Nearby Interaction peer sessions.

Measurement capabilities depend on both the capabilities of a person’s device and of the peer device they’re connecting to. Although someone might have a second generation UWB chip-equipped device, the peer devices they want to interact with might only support the first generation UWB chip.

Possible interactions between first generation and second generation UWB chips, and third-party MFI devices, include:

Supports multiple Nearby Interaction accessory sessions when communicating with third-party MFI chipsets.

Supports one Nearby Interaction peer EDM session and multiple Nearby Interaction peer sessions when communicating with second generation UWB-equipped devices.

Supports multiple Nearby Interaction accessory sessions when communicating with third-party MFI chipsets

> **Note**:  For more information on the MFI program, see the [`Nearby Interaction Accessory Protocol Specification`](https://developer.apple.comhttps://developer.apple.com/nearby-interaction/specification/).

Design your app with appropriate fallback options for interacting with devices that aren’t capable of EDM. For example, you could choose to show a limited experience that’s backwards compatible with first generation devices or, depending on your app’s intention, restrict interactions with peer devices that aren’t capable of using EDM. To identify a peer device’s measurement capabilities, query the [`deviceCapabilities`](nidiscoverytoken/devicecapabilities.md) property of an [`NIDiscoveryToken`](nidiscoverytoken.md). For an example that demonstrates limiting interactions to compatible devices, see [`Finding devices with precision`](finding-devices-with-precision.md).

Because EDM uses a new communications protocol, Nearby Interaction only supports one extended distance measurement session on a device at any given time. An EDM session can work concurrently with multiple legacy Nearby Interaction sessions on the same device.

The system may interrupt and pause an EDM session if required for critical use, such as when an authorized person uses Find My to locate another person’s device that’s in an EDM session. Additionally, the system may suspend EDM sessions when a person launches the Find My app. The app can listen for a [`sessionSuspensionEnded(_:)`](nisessiondelegate/sessionsuspensionended(_:).md) callback to determine when the app can resume the EDM session.

##### Locate Devices Using Ranging

The EDM support that the Nearby Interaction framework provides enables a new communication protocol that measures distances between devices using rapid packet exchanges. As a result, it’s susceptible to various wireless signal propagation effects. Most notably, obstruction between the two devices and reflections from the ground, walls, and parts of the local environment that affect the quality of distance measurements. These effects can significantly affect measurement quality at the longer measurement distances enabled by EDM. By design, Nearby Interaction tunes EDM to output measurements to your app at longer operating ranges. If your app requires high quality direction and distance measurements for the longer measurement distances enabled by EDM, estimate the quality of measurements and provide different user experiences.

The following example demonstrates a quality estimator for direction measurements is the `MeasurementQualityEstimator`:

```swift
    class MeasurementQualityEstimator {

        // Define the criteria that qualify a peer with "good" characteristics:
        // these include:

        // A time window, in seconds.
        let freshnessWindow = TimeInterval(floatLiteral: 2.0)
        // A minimum number of samples in that time window.
        let minSamples: Int = 8
        // A maximim distance, in meters.
        let maxDistance: Float = 50
        // A minimum distance, in meters.
        let closeDistance: Float = 10
    
        // A buffer to hold the individual quality measurements.
        private var measurements: [TimedNIObject] = []
    
        // An enumeration that defines levels of peer quality.
        enum MeasurementQuality {
            // The peer fails to meet any of the measurement quality criteria.
            case unknown

            // The extended distance measurements indicate the peer iPhone or device
            // satisfies the criteria for "good" quality and falls inside the
            // minimum and maximum acceptable distance.
            case good

            // The extended distance measurements indicate the current device
            // satisfies the criteria for being "close" to the peer iPhone or device.
            case close
        }

        // A structure that captures the range of a peer at a specific time.
        struct TimedNIObject {
            let time: TimeInterval
            let distance: Float
        }

        func estimateQuality(update: NINearbyObject?) -> MeasurementQuality {
            let timeNow = NSDate().timeIntervalSinceReferenceDate
            if let distance = update?.distance {
                if let lastMeasureMent = measurements.last {
                    if lastMeasureMent.distance != distance {
                        // Before adding new measurement to the buffer, 
                        // check if the reported distance is unique.
                        measurements.append(TimedNIObject(time: timeNow, distance: distance))
                    }
                } else {
                    // If the buffer is empty, unconditionally add the new measurement.
                    measurements.append(TimedNIObject(time: timeNow, distance: distance))
                }
            }
            let validTimestamp = timeNow - freshnessWindow
            measurements.removeAll { $0.time < validTimestamp }
            if measurements.count > minSamples, let lastDistance = measurements.last?.distance {
                if lastDistance <= closeDistance { return .close }
                return lastDistance < maxDistance ? .good : .unknown
            }
            return .unknown
        }
    }   
```

This class is a part of the Finding devices with precision sample for iOS 17 that demonstrates measurement quality estimation on devices capable of EDM. This estimator determines measurements are high quality if the framework generates eight or more distinct measurements in the last two seconds, and if the measurements are within a distance threshold of 50 meters. Experiment with different measurement quality metrics to vet the results to meet your app’s intended use cases.

iOS 16 and watchOS 9 introduced an API update to Nearby Interaction for locating stationary devices with high precision aided by an [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession). With the EDM capabilities introduced in iOS 17 and watchOS 10, second generation UWB equipped devices can locate moving devices that also have the second generation UWB chip.

##### Measure the Distance Between Devices

In iOS 14 and watchOS 8 and later, devices equipped with the first generation UWB chip are capable of precise distance measurement through the Nearby Interaction Framework. Devices supporting [`ARKit`](https://developer.apple.com/documentation/ARKit) can locate stationary objects or devices. Devices equipped with the second generation UWB chip are capable of EDM. Pairs of devices supporting both extended distance measurement and Camera Assistance have the ability to locate moving devices. You can query these capabilities through the [`deviceCapabilities`](nisession/devicecapabilities.md) property check.

To check a device’s EDM capability:

```swift
    if NISession.deviceCapabilities.supportsExtendedDistanceMeasurement {
        // This device supports EDM.
    } else {
        // Implement a fallback strategy.
    }
```

To determine if a peer device supports EDM, examine the peer’s [`NIDiscoveryToken`](nidiscoverytoken.md):

```swift
    if token.deviceCapabilities.supportsExtendedDistanceMeasurement {
        // The peer has EDM capability.
    } else {
        // Fall back to first generation UWB chip capabilities.
    }
```

If both sides support EDM, they can run [`NISession`](nisession.md) with the configuration that has EDM enabled, as shown in the example below:

```swift
    let config = NINearbyPeerConfiguration(peerToken: token)
    config.isCameraAssistanceEnabled = true
    if #available(iOS 17.0, watchOS 10.0, *) {
        guard NISession.deviceCapabilities.supportsExtendedDistanceMeasurement else {
           NSLog("This device isn't capable of finding visitors.")
           return
        }
        guard token.deviceCapabilities.supportsExtendedDistanceMeasurement else {
           NSLog("Peer device \(peer.displayName) isn't capable of finding visitors.")
           return
        }                   
       config.isExtendedDistanceMeasurementEnabled = true
       NSLog("NISession can use extended distance measurement.")                
    }
```

## See Also

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)
  Measure the relative position of a nearby device and coach the user to sustain interaction.
- [Finding devices with precision](finding-devices-with-precision.md)
  Leverage the spatial awareness of ARKit and Apple Ultra Wideband Chips in your app to guide users to a nearby device.
- [Implementing Interactions Between Users in Close Proximity](implementing-interactions-between-users-in-close-proximity.md)
  Enable devices to access relative positioning information.
- [Discovering peers with Multipeer Connectivity](discovering-peers-with-multipeer-connectivity.md)
  Exchange discovery tokens over the local network.
- [class NINearbyPeerConfiguration](ninearbypeerconfiguration.md)
  A configuration that enables interaction between iPhone or Apple Watch devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NearbyInteraction/extending-advanced-direction-finding-and-ranging)*