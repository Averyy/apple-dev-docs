# startMonitoring(for:)

**Framework**: Core Location  
**Kind**: method

Starts monitoring the specified region.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func startMonitoring(for region: CLRegion)
```

## Mentions

- [Monitoring the user’s proximity to geographic regions](monitoring-the-user-s-proximity-to-geographic-regions.md)
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)

#### Discussion

You must call this method once for each region you want to monitor. If an existing region with the same identifier is already being monitored by the app, the old region is replaced by the new one. The regions you add using this method are shared by all location manager objects in your app and stored in the [`monitoredRegions`](cllocationmanager/monitoredregions.md) property.

Region events are delivered to the [`locationManager(_:didEnterRegion:)`](cllocationmanagerdelegate/locationmanager(_:didenterregion:).md) and [`locationManager(_:didExitRegion:)`](cllocationmanagerdelegate/locationmanager(_:didexitregion:).md) methods of your delegate. If there is an error, the location manager calls the [`locationManager(_:monitoringDidFailFor:withError:)`](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md) method of your delegate instead.

An app can register up to 20 regions at a time. In order to report region changes in a timely manner, the region monitoring service requires network connectivity.

In iOS 6, regions with a radius between 1 and 400 meters work better on iPhone 4S or later devices. (In iOS 5, regions with a radius between 1 and 150 meters work better on iPhone 4S and later devices.) On these devices, an app can expect to receive the appropriate region entered or region exited notification within 3 to 5 minutes on average, if not sooner.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## Parameters

- `region`: The region object that defines the boundary to monitor. This parameter must not be  .

## See Also

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
- [func disallowDeferredLocationUpdates()](cllocationmanager/disallowdeferredlocationupdates.md)
  Cancels the deferral of location updates for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoring(for:))*