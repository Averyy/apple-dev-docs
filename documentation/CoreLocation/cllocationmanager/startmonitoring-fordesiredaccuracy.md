# startMonitoring(for:desiredAccuracy:)

**Framework**: Core Location  
**Kind**: method

Starts monitoring the specified region for boundary crossings.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func startMonitoring(for region: CLRegion, desiredAccuracy accuracy: CLLocationAccuracy)
```

#### Discussion

You must call this method separately for each region you want to monitor. If an existing region with the same identifier is already being monitored by the app, the old region is replaced by the new one. The regions you add using this method are shared by all location manager objects in your app and stored in the [`monitoredRegions`](cllocationmanager/monitoredregions.md) property.

If you begin monitoring a region and your app is subsequently terminated, the system automatically relaunches it into the background if the region boundary is crossed. In such a case, the options dictionary passed to the [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)) method of your app delegate contains the key [`location`](https://developer.apple.com/documentation/UIKit/UIApplication/LaunchOptionsKey/location) to indicate that your app was launched because of a location-related event. In addition, creating a new location manager and assigning a delegate results in the delivery of the corresponding region messages. The newly created location manager’s [`location`](cllocationmanager/location.md) property also contains the current location even if location services are not enabled.

Region events are delivered to the [`locationManager(_:didEnterRegion:)`](cllocationmanagerdelegate/locationmanager(_:didenterregion:).md) and [`locationManager(_:didExitRegion:)`](cllocationmanagerdelegate/locationmanager(_:didexitregion:).md) methods of your delegate. If there is an error, the location manager calls the [`locationManager(_:monitoringDidFailFor:withError:)`](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md) method of your delegate instead.

## Parameters

- `region`: The region object that defines the boundary to monitor. This parameter must not be  .
- `accuracy`: The distance past the border (measured in meters) at which to generate notifications. You can use this value to prevent the delivery of multiple notifications when the user is close to the border’s edge.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoring(for:desiredaccuracy:))*