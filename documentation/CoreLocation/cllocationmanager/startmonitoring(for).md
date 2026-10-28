# startMonitoring(for:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Starts monitoring the specified region.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.2

> **Deprecated**: Use [`addConditionForMonitoring:identifier:`](../clmonitor-6ynwz/addconditionformonitoring_identifier_.md) instead.

## Declaration

```swift
func startMonitoring(for region: CLRegion)
```

```objc
- (void) startMonitoringForRegion:(CLRegion *) region;
```

## Mentions

- [Determining the proximity to an iBeacon device](../determining-the-proximity-to-an-ibeacon-device.md)
- [Monitoring the user’s proximity to geographic regions](../monitoring-the-user-s-proximity-to-geographic-regions.md)

## Discussion

You must call this method once for each region you want to monitor. If an existing region with the same identifier is already being monitored by the app, the old region is replaced by the new one. The regions you add using this method are shared by all location manager objects in your app and stored in the [`monitoredRegions`](./monitoredregions.md) property.

Region events are delivered to the [`locationManager(_:didEnterRegion:)`](../cllocationmanagerdelegate/locationmanager%28_,didenterregion%29.md) and [`locationManager(_:didExitRegion:)`](../cllocationmanagerdelegate/locationmanager%28_,didexitregion%29.md) methods of your delegate. If there is an error, the location manager calls the [`locationManager(_:monitoringDidFailFor:withError:)`](../cllocationmanagerdelegate/locationmanager%28_,monitoringdidfailfor,witherror%29.md) method of your delegate instead.

An app can register up to 20 regions at a time. In order to report region changes in a timely manner, the region monitoring service requires network connectivity.

In iOS 6, regions with a radius between 1 and 400 meters work better on iPhone 4S or later devices. (In iOS 5, regions with a radius between 1 and 150 meters work better on iPhone 4S and later devices.) On these devices, an app can expect to receive the appropriate region entered or region exited notification within 3 to 5 minutes on average, if not sooner.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## Parameters

- `region`: The region object that defines the boundary to monitor. This parameter must not be `nil`.

## See Also

### Methods
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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoring(for:))*