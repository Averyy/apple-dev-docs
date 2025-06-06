# CMWaterSubmersionManager

**Framework**: Core Motion  
**Kind**: class

An object for managing the collection of pressure and temperature data during submersion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CMWaterSubmersionManager
```

## Mentions

- [Accessing submersion data](accessing-submersion-data.md)

#### Overview

Use this class to receive live depth, water pressure, and water temperature data on Apple Watch Ultra.

Start by assigning a usage description using the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app target’s information property list. You also need to include an entitlement to access the live submersion data.

To access data for dives with a maximum depth of 6 m, add the Shallow Depth and Pressure capability to your app. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

To enable a maximum depth of 40 m, you must apply for the full Submerged Depth and Pressure entitlement. For more information, see [`Express interest in the Submerged Depth and Pressure API`](https://developer.apple.comhttps://developer.apple.com/contact/request/submerged-depth-pressure-api/).

> **Note**:  As the wearer approaches the maximum depth, the system sends a measurement with an [`CMWaterSubmersionMeasurement.DepthState.approachingMaxDepth`](cmwatersubmersionmeasurement/depthstate/approachingmaxdepth.md) submersion state. When they pass the maximum depth, it sends a [`CMWaterSubmersionMeasurement.DepthState.pastMaxDepth`](cmwatersubmersionmeasurement/depthstate/pastmaxdepth.md) state, and if they continue to descent past the maximum depth, it sends a [`CMWaterSubmersionMeasurement.DepthState.sensorDepthError`](cmwatersubmersionmeasurement/depthstate/sensordeptherror.md) state.

 As the wearer approaches the maximum depth, the system sends a measurement with an [`CMWaterSubmersionMeasurement.DepthState.approachingMaxDepth`](cmwatersubmersionmeasurement/depthstate/approachingmaxdepth.md) submersion state. When they pass the maximum depth, it sends a [`CMWaterSubmersionMeasurement.DepthState.pastMaxDepth`](cmwatersubmersionmeasurement/depthstate/pastmaxdepth.md) state, and if they continue to descent past the maximum depth, it sends a [`CMWaterSubmersionMeasurement.DepthState.sensorDepthError`](cmwatersubmersionmeasurement/depthstate/sensordeptherror.md) state.

Next, check whether submersion data is available.

```swift
guard CMWaterSubmersionManager.waterSubmersionAvailable else {
    return false
}
```

If the [`waterSubmersionAvailable`](cmwatersubmersionmanager/watersubmersionavailable.md) property is [`true`](https://developer.apple.com/documentation/swift/true), instantiate a [`CMWaterSubmersionManager`](cmwatersubmersionmanager.md) object and assign a delegate.

```swift
// Instantiate the submersion manager.
submersionManager = CMWaterSubmersionManager()


// Assign the submersion manager delegate.
submersionManager.delegate = self
```

Your delegate then begins receiving updates from the system. For more information, see [`Accessing submersion data`](accessing-submersion-data.md).

## Topics

### Setting the delegate
- [var delegate: (any CMWaterSubmersionManagerDelegate)?](cmwatersubmersionmanager/delegate.md)
  The object that receives updates about submersion data and events.
### Checking availability and authorization
- [class var waterSubmersionAvailable: Bool](cmwatersubmersionmanager/watersubmersionavailable.md)
  A Boolean value indicating whether the current device supports the submersion manager.
- [class var authorizationStatus: CMAuthorizationStatus](cmwatersubmersionmanager/authorizationstatus.md)
  A value indicating whether the app has user authorization to receive submersion data.
### Accessing the maximum depth
- [var maximumDepth: Measurement<UnitLength>?](cmwatersubmersionmanager/maximumdepth.md)
  The maximum depth supported by the water submersion manager.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Accessing submersion data](accessing-submersion-data.md)
  Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- [protocol CMWaterSubmersionManagerDelegate](cmwatersubmersionmanagerdelegate.md)
  A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.
- [class CMWaterSubmersionEvent](cmwatersubmersionevent.md)
  An event indicating that the device’s submersion state has changed.
- [class CMWaterSubmersionMeasurement](cmwatersubmersionmeasurement.md)
  An update that contains data about the pressure and depth.
- [class CMWaterTemperature](cmwatertemperature.md)
  An update that contains data about the water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)*