# regionMonitoringEnabled()

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether region monitoring is currently enabled.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
class func regionMonitoringEnabled() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if region monitoring is available and is currently enabled; [`false`](https://developer.apple.com/documentation/Swift/false) if it is unavailable or not enabled.

#### Discussion

In iOS, the user can enable or disable location services (including region monitoring) using the controls in Settings > Location Services.

You should check the return value of this method before starting region monitoring updates to determine whether the user currently allows location services to be used at all. If this method returns [`false`](https://developer.apple.com/documentation/Swift/false) and you start region monitoring updates anyway, the Core Location framework prompts the user to confirm asking whether location services should be reenabled.

This method does not check to see if region monitoring capabilities are actually supported by the device. Therefore, you should also check the return value of the [`regionMonitoringAvailable()`](cllocationmanager/regionmonitoringavailable().md) class method before attempting to start region monitoring services.

## See Also

- [func startMonitoring(for: CLRegion)](cllocationmanager/startmonitoring(for:).md)
  Starts monitoring the specified region.
- [func stopMonitoring(for: CLRegion)](cllocationmanager/stopmonitoring(for:).md)
  Stops monitoring the specified region.
- [class func regionMonitoringAvailable() -> Bool](cllocationmanager/regionmonitoringavailable.md)
  Returns a Boolean value indicating whether region monitoring is supported on the current device.
- [class func authorizationStatus() -> CLAuthorizationStatus](cllocationmanager/authorizationstatus.md)
  Returns the app’s authorization status for using location services.
- [func startMonitoring(for: CLRegion, desiredAccuracy: CLLocationAccuracy)](cllocationmanager/startmonitoring(for:desiredaccuracy:).md)
  Starts monitoring the specified region for boundary crossings.
- [func requestState(for: CLRegion)](cllocationmanager/requeststate(for:).md)
  Retrieves the state of a region asynchronously.
- [func startRangingBeacons(in: CLBeaconRegion)](cllocationmanager/startrangingbeacons(in:).md)
  Starts the delivery of notifications for the specified beacon region.
- [func stopRangingBeacons(in: CLBeaconRegion)](cllocationmanager/stoprangingbeacons(in:).md)
  Stops the delivery of notifications for the specified beacon region.
- [class func deferredLocationUpdatesAvailable() -> Bool](cllocationmanager/deferredlocationupdatesavailable.md)
  Returns a Boolean value indicating whether the device supports deferred location updates.
- [func allowDeferredLocationUpdates(untilTraveled: CLLocationDistance, timeout: TimeInterval)](cllocationmanager/allowdeferredlocationupdates(untiltraveled:timeout:).md)
  Asks the location manager to defer the delivery of location updates until the specified criteria are met.
- [func disallowDeferredLocationUpdates()](cllocationmanager/disallowdeferredlocationupdates.md)
  Cancels the deferral of location updates for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/regionmonitoringenabled())*