# disallowDeferredLocationUpdates()

**Framework**: Core Location  
**Kind**: method

Cancels the deferral of location updates for this app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func disallowDeferredLocationUpdates()
```

#### Discussion

Call this method if you previously deferred location event delivery using the [`allowDeferredLocationUpdates(untilTraveled:timeout:)`](cllocationmanager/allowdeferredlocationupdates(untiltraveled:timeout:).md) method and now want to resume the delivery of events at normal intervals.

## See Also

- [func startMonitoring(for: CLRegion)](cllocationmanager/startmonitoring(for:).md)
  Starts monitoring the specified region.
- [func stopMonitoring(for: CLRegion)](cllocationmanager/stopmonitoring(for:).md)
  Stops monitoring the specified region.
- [class func regionMonitoringAvailable() -> Bool](cllocationmanager/regionmonitoringavailable.md)
  Returns a Boolean value indicating whether region monitoring is supported on the current device.
- [class func regionMonitoringEnabled() -> Bool](cllocationmanager/regionmonitoringenabled.md)
  Returns a Boolean value indicating whether region monitoring is currently enabled.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/disallowdeferredlocationupdates())*