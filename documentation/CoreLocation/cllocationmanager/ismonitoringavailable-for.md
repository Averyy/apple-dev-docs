# isMonitoringAvailable(for:)

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether the device supports region monitoring using the specified class.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
class func isMonitoringAvailable(for regionClass: AnyClass) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device is capable of monitoring regions using the specified class or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

The availability of region monitoring support is dependent on the hardware present on the device. This method does not take into account the availability of location services or the fact that the user might have disabled them for the app or system; you must determine your app’s authorization status separately.

## Parameters

- `regionClass`: A region monitoring class from the MapKit framework. This class must descend from the   class.

## See Also

- [class func significantLocationChangeMonitoringAvailable() -> Bool](cllocationmanager/significantlocationchangemonitoringavailable.md)
  Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [class func headingAvailable() -> Bool](cllocationmanager/headingavailable.md)
  Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [var isAuthorizedForWidgetUpdates: Bool](cllocationmanager/isauthorizedforwidgetupdates.md)
  A Boolean value that indicates whether a widget is eligible to receive location updates.
- [var accuracyAuthorization: CLAccuracyAuthorization](cllocationmanager/accuracyauthorization.md)
  A value that indicates the level of location accuracy the app has permission to use.
- [class func isRangingAvailable() -> Bool](cllocationmanager/israngingavailable.md)
  Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [class func locationServicesEnabled() -> Bool](cllocationmanager/locationservicesenabled.md)
  Returns a Boolean value indicating whether location services are enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/ismonitoringavailable(for:))*