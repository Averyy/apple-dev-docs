# Deprecated symbols

**Framework**: Core Location  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Properties
- [var headingAvailable: Bool](./cllocationmanager/headingavailable-swift.property.md)
  A Boolean value indicating whether the location manager is able to generate heading-related events.
- [var locationServicesEnabled: Bool](./cllocationmanager/locationservicesenabled-swift.property.md)
  A Boolean value indicating whether location services are enabled on the device.
- [var purpose: String?](./cllocationmanager/purpose.md)
  An app-provided string that describes the reason for using location services.
- [var rangedRegions: Set<CLRegion>](./cllocationmanager/rangedregions.md)
  The set of regions currently being tracked using ranging.
### Methods
- [func startMonitoring(for: CLRegion)](./cllocationmanager/startmonitoring%28for%29.md)
  Starts monitoring the specified region.
- [func stopMonitoring(for: CLRegion)](./cllocationmanager/stopmonitoring%28for%29.md)
  Stops monitoring the specified region.
- [class func regionMonitoringAvailable() -> Bool](./cllocationmanager/regionmonitoringavailable%28%29.md)
  Returns a Boolean value indicating whether region monitoring is supported on the current device.
- [class func regionMonitoringEnabled() -> Bool](./cllocationmanager/regionmonitoringenabled%28%29.md)
  Returns a Boolean value indicating whether region monitoring is currently enabled.
- [class func authorizationStatus() -> CLAuthorizationStatus](./cllocationmanager/authorizationstatus%28%29.md)
  Returns the app’s authorization status for using location services.
- [func startMonitoring(for: CLRegion, desiredAccuracy: CLLocationAccuracy)](./cllocationmanager/startmonitoring%28for,desiredaccuracy%29.md)
  Starts monitoring the specified region for boundary crossings.
- [func requestState(for: CLRegion)](./cllocationmanager/requeststate%28for%29.md)
  Retrieves the state of a region asynchronously.
- [func startRangingBeacons(in: CLBeaconRegion)](./cllocationmanager/startrangingbeacons%28in%29.md)
  Starts the delivery of notifications for the specified beacon region.
- [func stopRangingBeacons(in: CLBeaconRegion)](./cllocationmanager/stoprangingbeacons%28in%29.md)
  Stops the delivery of notifications for the specified beacon region.
- [class func deferredLocationUpdatesAvailable() -> Bool](./cllocationmanager/deferredlocationupdatesavailable%28%29.md)
  Returns a Boolean value indicating whether the device supports deferred location updates.
- [func allowDeferredLocationUpdates(untilTraveled: CLLocationDistance, timeout: TimeInterval)](./cllocationmanager/allowdeferredlocationupdates%28untiltraveled,timeout%29.md)
  Asks the location manager to defer the delivery of location updates until the specified criteria are met.
- [func disallowDeferredLocationUpdates()](./cllocationmanager/disallowdeferredlocationupdates%28%29.md)
  Cancels the deferral of location updates for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/deprecated-symbols)*