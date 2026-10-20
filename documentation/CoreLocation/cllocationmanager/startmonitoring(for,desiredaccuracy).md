# startMonitoring(for:desiredAccuracy:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Starts monitoring the specified region for boundary crossings.

**Availability**:
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use [`startMonitoring(for:)`](./startmonitoring%28for%29.md) instead.

## Declaration

```swift
func startMonitoring(for region: CLRegion, desiredAccuracy accuracy: CLLocationAccuracy)
```

```objc
- (void) startMonitoringForRegion:(CLRegion *) region desiredAccuracy:(CLLocationAccuracy) accuracy;
```

#### Discussion

You must call this method separately for each region you want to monitor. If an existing region with the same identifier is already being monitored by the app, the old region is replaced by the new one. The regions you add using this method are shared by all location manager objects in your app and stored in the [`monitoredRegions`](./monitoredregions.md) property.

If you begin monitoring a region and your app is subsequently terminated, the system automatically relaunches it into the background if the region boundary is crossed. In such a case, the options dictionary passed to the [`application(_:didFinishLaunchingWithOptions:)`](../../UIKit/uiapplicationdelegate/application%28_,didfinishlaunchingwithoptions%29.md) method of your app delegate contains the key [`location`](../../UIKit/uiapplication/launchoptionskey/location.md) to indicate that your app was launched because of a location-related event. In addition, creating a new location manager and assigning a delegate results in the delivery of the corresponding region messages. The newly created location manager’s [`location`](./location.md) property also contains the current location even if location services are not enabled.

Region events are delivered to the [`locationManager(_:didEnterRegion:)`](../cllocationmanagerdelegate/locationmanager%28_,didenterregion%29.md) and [`locationManager(_:didExitRegion:)`](../cllocationmanagerdelegate/locationmanager%28_,didexitregion%29.md) methods of your delegate. If there is an error, the location manager calls the [`locationManager(_:monitoringDidFailFor:withError:)`](../cllocationmanagerdelegate/locationmanager%28_,monitoringdidfailfor,witherror%29.md) method of your delegate instead.

## Parameters

- `region`: The region object that defines the boundary to monitor. This parameter must not be `nil`.
- `accuracy`: The distance past the border (measured in meters) at which to generate notifications. You can use this value to prevent the delivery of multiple notifications when the user is close to the border’s edge.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoring(for:desiredaccuracy:))*