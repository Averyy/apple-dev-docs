# regionMonitoringEnabled()

**Framework**: Core Location  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether region monitoring is currently enabled.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 4.0+ - Deprecated in 6.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`isMonitoringAvailable(for:)`](./ismonitoringavailable%28for%29.md) instead.

## Declaration

```swift
class func regionMonitoringEnabled() -> Bool
```

```objc
+ (BOOL) regionMonitoringEnabled;
```

#### Return Value

[`true`](../../Swift/true.md) if region monitoring is available and is currently enabled; [`false`](../../Swift/false.md) if it is unavailable or not enabled.

#### Discussion

In iOS, the user can enable or disable location services (including region monitoring) using the controls in Settings > Location Services.

You should check the return value of this method before starting region monitoring updates to determine whether the user currently allows location services to be used at all. If this method returns [`false`](../../Swift/false.md) and you start region monitoring updates anyway, the Core Location framework prompts the user to confirm asking whether location services should be reenabled.

This method does not check to see if region monitoring capabilities are actually supported by the device. Therefore, you should also check the return value of the [`regionMonitoringAvailable()`](./regionmonitoringavailable%28%29.md) class method before attempting to start region monitoring services.

## See Also

### Methods
- [func startMonitoring(for: CLRegion)](./startmonitoring%28for%29.md)
  Starts monitoring the specified region.
- [func stopMonitoring(for: CLRegion)](./stopmonitoring%28for%29.md)
  Stops monitoring the specified region.
- [class func regionMonitoringAvailable() -> Bool](./regionmonitoringavailable%28%29.md)
  Returns a Boolean value indicating whether region monitoring is supported on the current device.
- [class func authorizationStatus() -> CLAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns the app’s authorization status for using location services.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/regionmonitoringenabled())*