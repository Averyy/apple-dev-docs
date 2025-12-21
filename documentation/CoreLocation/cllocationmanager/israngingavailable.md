# isRangingAvailable()

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func isRangingAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports ranging or [`false`](https://developer.apple.com/documentation/Swift/false) if it does not.

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
- [class func locationServicesEnabled() -> Bool](cllocationmanager/locationservicesenabled.md)
  Returns a Boolean value indicating whether location services are enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/israngingavailable())*