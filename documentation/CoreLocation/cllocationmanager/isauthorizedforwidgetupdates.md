# isAuthorizedForWidgetUpdates

**Framework**: Core Location  
**Kind**: property

A Boolean value that indicates whether a widget is eligible to receive location updates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isAuthorizedForWidgetUpdates: Bool { get }
```

#### Discussion

This property is `true` when either of the following is true:

- The app’s authorization status is [`CLAuthorizationStatus.authorizedAlways`](clauthorizationstatus/authorizedalways.md).
- The app’s authorization status is [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md) and the user agrees to extend the app’s authorization status to widgets.

> **Note**:  For apps that use [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md), after the user agrees to extend an app’s authorization status to widgets, the app’s Location Services settings indicate While Using the App or Widgets as the active access level.

 For apps that use [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md), after the user agrees to extend an app’s authorization status to widgets, the app’s Location Services settings indicate While Using the App or Widgets as the active access level.

For details about using location information in widgets with [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md), see [`Accessing location information in widgets`](https://developer.apple.com/documentation/WidgetKit/Accessing-Location-Information-in-Widgets).

## See Also

- [class func significantLocationChangeMonitoringAvailable() -> Bool](cllocationmanager/significantlocationchangemonitoringavailable.md)
  Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [class func headingAvailable() -> Bool](cllocationmanager/headingavailable.md)
  Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [var accuracyAuthorization: CLAccuracyAuthorization](cllocationmanager/accuracyauthorization.md)
  A value that indicates the level of location accuracy the app has permission to use.
- [class func isMonitoringAvailable(for: AnyClass) -> Bool](cllocationmanager/ismonitoringavailable(for:).md)
  Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [class func isRangingAvailable() -> Bool](cllocationmanager/israngingavailable.md)
  Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [class func locationServicesEnabled() -> Bool](cllocationmanager/locationservicesenabled.md)
  Returns a Boolean value indicating whether location services are enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/isauthorizedforwidgetupdates)*