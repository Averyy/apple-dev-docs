# startRangingBeacons(in:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Starts the delivery of notifications for the specified beacon region.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 11.0+ - Deprecated in 11.0

> **Deprecated**: Use [`startRangingBeacons(satisfying:)`](./startrangingbeacons%28satisfying%29.md) instead.

## Declaration

```swift
func startRangingBeacons(in region: CLBeaconRegion)
```

```objc
- (void) startRangingBeaconsInRegion:(CLBeaconRegion *) region;
```

## Mentions

- [Determining the proximity to an iBeacon device](../determining-the-proximity-to-an-ibeacon-device.md)

## Discussion

Once registered, the location manager reports any encountered beacons to its delegate by calling the [`locationManager(_:didRangeBeacons:in:)`](../cllocationmanagerdelegate/locationmanager%28_,didrangebeacons,in%29.md) method. If there is an error registering the specified beacon region, the location manager calls its delegate’s [`locationManager(_:rangingBeaconsDidFailFor:withError:)`](../cllocationmanagerdelegate/locationmanager%28_,rangingbeaconsdidfailfor,witherror%29.md) method and provides the appropriate error information.

## Parameters

- `region`: The region object that defines the identifying information for the targeted beacons. The number of beacons represented by this region object depends on which identifier values you use to initialize it. Beacons must match all of the identifiers you specify. This method copies the region information it needs from the object you provide.

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
- [class func authorizationStatus() -> CLAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns the app’s authorization status for using location services.
- [func startMonitoring(for: CLRegion, desiredAccuracy: CLLocationAccuracy)](./startmonitoring%28for,desiredaccuracy%29.md)
  Starts monitoring the specified region for boundary crossings.
- [func requestState(for: CLRegion)](./requeststate%28for%29.md)
  Retrieves the state of a region asynchronously.
- [func stopRangingBeacons(in: CLBeaconRegion)](./stoprangingbeacons%28in%29.md)
  Stops the delivery of notifications for the specified beacon region.
- [class func deferredLocationUpdatesAvailable() -> Bool](./deferredlocationupdatesavailable%28%29.md)
  Returns a Boolean value indicating whether the device supports deferred location updates.
- [func allowDeferredLocationUpdates(untilTraveled: CLLocationDistance, timeout: TimeInterval)](./allowdeferredlocationupdates%28untiltraveled,timeout%29.md)
  Asks the location manager to defer the delivery of location updates until the specified criteria are met.
- [func disallowDeferredLocationUpdates()](./disallowdeferredlocationupdates%28%29.md)
  Cancels the deferral of location updates for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startrangingbeacons(in:))*