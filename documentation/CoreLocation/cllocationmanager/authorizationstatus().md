# authorizationStatus()

**Framework**: Core Location  
**Kind**: method  
**Role**: Type Method

Returns the app’s authorization status for using location services.

**Availability**:
- iOS 4.2+ - Deprecated in 14.0
- iPadOS 4.2+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.7+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`authorizationStatus`](./authorizationstatus-swift.property.md) instance property with [`locationManagerDidChangeAuthorization(_:)`](../cllocationmanagerdelegate/locationmanagerdidchangeauthorization%28_%29.md) instead.

## Declaration

```swift
class func authorizationStatus() -> CLAuthorizationStatus
```

```objc
+ (CLAuthorizationStatus) authorizationStatus;
```

## Return Value

A value indicating whether the app is authorized to use location services.

## Discussion

The system is guaranteed to call the delegate method with the app’s initial authorization state and all authorization status changes.

The system manages the authorization status of a given app according to several factors. Users must authorize the app to use location services explicitly, and location services must be enabled in Settings > Privacy. See [Choosing the  Location Services Authorization to Request](../../BundleResources/choosing-the-location-services-authorization-to-request.md) for more information.

## See Also

### Methods
- [func startMonitoring(for: CLRegion)](./startmonitoring%28for%29.md)
  Starts monitoring the specified region.
- [func stopMonitoring(for: CLRegion)](./stopmonitoring%28for%29.md)
  Stops monitoring the specified region.
- [class func regionMonitoringAvailable() -> Bool](./regionmonitoringavailable%28%29.md)
  Returns a Boolean value indicating whether region monitoring is supported on the current device.
- [class func regionMonitoringEnabled() -> Bool](./regionmonitoringenabled%28%29.md)
  Returns a Boolean value indicating whether region monitoring is currently enabled.
- [func startMonitoring(for: CLRegion, desiredAccuracy: CLLocationAccuracy)](./startmonitoring%28for,desiredaccuracy%29.md)
  Starts monitoring the specified region for boundary crossings.
- [func requestState(for: CLRegion)](./requeststate%28for%29.md)
  Retrieves the state of a region asynchronously.
- [func startRangingBeacons(in: CLBeaconRegion)](./startrangingbeacons%28in%29.md)
  Starts the delivery of notifications for the specified beacon region.
- [func stopRangingBeacons(in: CLBeaconRegion)](./stoprangingbeacons%28in%29.md)
  Stops the delivery of notifications for the specified beacon region.
- [class func deferredLocationUpdatesAvailable() -> Bool](./deferredlocationupdatesavailable%28%29.md)
  Returns a Boolean value indicating whether the device supports deferred location updates.
- [func allowDeferredLocationUpdates(untilTraveled: CLLocationDistance, timeout: TimeInterval)](./allowdeferredlocationupdates%28untiltraveled,timeout%29.md)
  Asks the location manager to defer the delivery of location updates until the specified criteria are met.
- [func disallowDeferredLocationUpdates()](./disallowdeferredlocationupdates%28%29.md)
  Cancels the deferral of location updates for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/authorizationstatus())*