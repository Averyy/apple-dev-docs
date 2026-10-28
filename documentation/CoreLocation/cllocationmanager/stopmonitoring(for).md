# stopMonitoring(for:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Stops monitoring the specified region.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.2

> **Deprecated**: Use [`removeConditionFromMonitoringWithIdentifier:`](../clmonitor-6ynwz/removeconditionfrommonitoringwithidentifier_.md) instead.

## Declaration

```swift
func stopMonitoring(for region: CLRegion)
```

```objc
- (void) stopMonitoringForRegion:(CLRegion *) region;
```

## Discussion

If the specified region object is not currently being monitored, this method has no effect. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## Parameters

- `region`: The region object currently being monitored. This parameter must not be `nil`.

## See Also

### Methods
- [func startMonitoring(for: CLRegion)](./startmonitoring%28for%29.md)
  Starts monitoring the specified region.
- [class func regionMonitoringAvailable() -> Bool](./regionmonitoringavailable%28%29.md)
  Returns a Boolean value indicating whether region monitoring is supported on the current device.
- [class func regionMonitoringEnabled() -> Bool](./regionmonitoringenabled%28%29.md)
  Returns a Boolean value indicating whether region monitoring is currently enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoring(for:))*