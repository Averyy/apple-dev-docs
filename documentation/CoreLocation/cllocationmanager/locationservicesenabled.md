# locationServicesEnabled()

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether location services are enabled on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func locationServicesEnabled() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if location services are enabled on the device; [`false`](https://developer.apple.com/documentation/swift/false) if they are not.

#### Discussion

Users can enable or disable location services by toggling the Location Services switch in Settings > Privacy.

- When users disable the switch, the system calls your delegate’s [`locationManager(_:didChangeAuthorization:)`](cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:).md) method with a denied authorization status ([`CLAuthorizationStatus.denied`](clauthorizationstatus/denied.md)).
- When users enable the switch, the system returns your app’s authorization to its previous state and calls your delegate’s [`locationManager(_:didChangeAuthorization:)`](cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:).md) method.

You are not required to call [`locationServicesEnabled()`](cllocationmanager/locationservicesenabled().md). However, If you wish to display instructions about enabling location services, you may check the return value of this method to find out if the services are disabled for the entire device, or just for your app.  If the result is `true`, provide instructions for enabling services for your app; otherwise, provide instructions for enabling the Location Services switch in Settings > Privacy.

If users disable or deny location services and you attempt to start location updates anyway, the location manager reports an error to its delegate. See [`locationManager(_:didFailWithError:)`](cllocationmanagerdelegate/locationmanager(_:didfailwitherror:).md) and [`locationManager(_:monitoringDidFailFor:withError:)`](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md) for more information.

## Topics

### Related Documentation
- [func locationManager(CLLocationManager, didFailWithError: any Error)](cllocationmanagerdelegate/locationmanager(_:didfailwitherror:).md)
  Tells the delegate that the location manager was unable to retrieve a location value.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md)
  Tells the delegate that a region monitoring error occurred.

## See Also

- [class func significantLocationChangeMonitoringAvailable() -> Bool](cllocationmanager/significantlocationchangemonitoringavailable.md)
  Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [class func headingAvailable() -> Bool](cllocationmanager/headingavailable.md)
  Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [var isAuthorizedForWidgetUpdates: Bool](cllocationmanager/isauthorizedforwidgetupdates.md)
  A Boolean value that indicates whether a widget is eligible to receive location updates.
- [var accuracyAuthorization: CLAccuracyAuthorization](cllocationmanager/accuracyauthorization.md)
  A value that indicates the level of location accuracy the app has permission to use.
- [class func isMonitoringAvailable(for: AnyClass) -> Bool](cllocationmanager/ismonitoringavailable(for:).md)
  Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [class func isRangingAvailable() -> Bool](cllocationmanager/israngingavailable.md)
  Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled())*