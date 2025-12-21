# headingAvailable()

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether the location manager is able to generate heading-related events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func headingAvailable() -> Bool
```

## Mentions

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if heading data is available; [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

#### Discussion

Heading data may not be available on all iOS-based devices. You should check the value returned by this method before asking the location manager to deliver heading-related events.

## See Also

- [class func significantLocationChangeMonitoringAvailable() -> Bool](cllocationmanager/significantlocationchangemonitoringavailable.md)
  Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [var isAuthorizedForWidgetUpdates: Bool](cllocationmanager/isauthorizedforwidgetupdates.md)
  A Boolean value that indicates whether a widget is eligible to receive location updates.
- [var accuracyAuthorization: CLAccuracyAuthorization](cllocationmanager/accuracyauthorization.md)
  A value that indicates the level of location accuracy the app has permission to use.
- [class func isMonitoringAvailable(for: AnyClass) -> Bool](cllocationmanager/ismonitoringavailable(for:).md)
  Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [class func isRangingAvailable() -> Bool](cllocationmanager/israngingavailable.md)
  Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [class func locationServicesEnabled() -> Bool](cllocationmanager/locationservicesenabled.md)
  Returns a Boolean value indicating whether location services are enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/headingavailable())*