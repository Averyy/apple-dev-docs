# Downlink time difference of arrival ranging

**Framework**: Nearby Interaction

Use anchor devices to improve the accuracy of indoor positioning.

#### Overview

Downlink Time-Difference-of-Arrival (DL-TDOA) is an Ultra Wideband (UWB) ranging strategy that can produce sub-meter location support for physical devices in a well-defined area. The solution works by installing physical devices, or *anchors*, within the deployment area. The anchors send messages to receiver devices that support DL-TDOA, such as iPhone, and the receivers use the messages to calculate their location by measuring the message time difference of arrival. The supported anchors as well as the framework’s anchor-interaction comply with the IEEE 802.15.4z standard.

> **Note**:  In iOS 27 and later, DL-TDOA no longer requires an entitlement.

#### Ask for Location Approval

DL-TDOA ranging requires your app to request the person’s location authorization. Before running a DL-TDOA session, use [`CLLocationManager`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager) to request location authorization:

```swift
func startDLTDOA() {
    // Request location authorization.
    // The system prompts the person if authorization status is not determined.
    locationManager.requestWhenInUseAuthorization()    
    // Check authorization status.
    let authStatus = locationManager.authorizationStatus
    guard authStatus == .authorizedWhenInUse || authStatus == .authorizedAlways else {
        print("Location authorization required for DL-TDOA.")
        return
    }
    // Configure the DL-TDOA session.
}
```

Add the [`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription) key to your app’s target properties in Xcode to support [`requestWhenInUseAuthorization()`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/requestWhenInUseAuthorization()). Add the [`NSLocationAlwaysAndWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription) key to your app’s target properties in Xcode to support [`requestAlwaysAuthorization()`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/requestAlwaysAuthorization()).

The system presents an authorization prompt to the person the first time your app requests authorization. On subsequent launches, the system checks the person’s previous authorization decision. If the person denies authorization, the DL-TDOA session stops with an error.

##### Specify a Discovery Method

To discover anchors in your deployment environment, specify the discovery method at the time of configuring your session by calling [`init(networkIdentifier:discoveryMethod:)`](nidltdoaconfiguration/init(networkidentifier:discoverymethod:).md). Your app needs to exclusively use either Wi-Fi or Bluetooth Low Energy to discover anchors. By specifying the technology, the framework focuses anchor interaction on the specified method throughout the life of the session. If you don’t specify the discovery method (by calling [`init(networkIdentifier:)`](nidltdoaconfiguration/init(networkidentifier:).md)), the discovery method defaults to [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](nidltdoaconfiguration/discoverymethod-swift.enum/bluetoothlowenergy.md).

##### Receive Measurements and Calculate the Devices Location

When a device receives a message from an anchor, the framework creates the measurement object [`NIDLTDOAMeasurement`](nidltdoameasurement.md) and provides it to your app by invoking the  [`session(_:didUpdateDLTDOA:)`](nisessiondelegate/session(_:didupdatedltdoa:).md) callback. The measurement contains the coordinates of the anchor in the physical environment and the time it takes the message to arrive. Your app uses the anchor’s coordinates and the elapsed message-transmission time to calculate the device’s location. The calculation consists of a comparison of measurements from multiple anchors, and in particular, the difference in their arrival time to the receiver.

##### Distinguish and Determine the Deployment Area

Provide a network identifier when instantiating this class to distinguish among different deployment areas when there are multiple such areas in the vicinity. The network identifier is the session ID in the anchor’s DL-TDOA configuration. Your app can infer the range of an anchor by changes in its signal strength. The anchor’s range, coordinates, and network ID together compose the bounds of the tracked area.

## Topics

### Configuration
- [class NIDLTDOAConfiguration](nidltdoaconfiguration.md)
  A configuration that enables Downlink Time-Difference-of-Arrival ranging.
### Measurements
- [class NIDLTDOAMeasurement](nidltdoameasurement.md)
  Information from a Downlink Time-Difference-of-Arrival anchor that you use to derive a range estimate.
- [enum NIDLTDOACoordinatesType](nidltdoacoordinatestype.md)
  The possible coordinate types for Downlink Time-Difference-of-Arrival measurement updates.
- [enum NIDLTDOAMeasurementType](nidltdoameasurementtype.md)
  The possible phases of downlink positioning signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/dl-tdoa-ranging)*