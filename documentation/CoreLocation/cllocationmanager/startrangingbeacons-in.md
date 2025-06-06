# startRangingBeacons(in:)

**Framework**: Core Location  
**Kind**: method

Starts the delivery of notifications for the specified beacon region.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func startRangingBeacons(in region: CLBeaconRegion)
```

## Mentions

- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)

#### Discussion

Once registered, the location manager reports any encountered beacons to its delegate by calling the [`locationManager(_:didRangeBeacons:in:)`](cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:).md) method. If there is an error registering the specified beacon region, the location manager calls its delegate’s [`locationManager(_:rangingBeaconsDidFailFor:withError:)`](cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:).md) method and provides the appropriate error information.

## Parameters

- `region`: The region object that defines the identifying information for the targeted beacons. The number of beacons represented by this region object depends on which identifier values you use to initialize it. Beacons must match all of the identifiers you specify. This method copies the region information it needs from the object you provide.

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
- [func stopRangingBeacons(in: CLBeaconRegion)](cllocationmanager/stoprangingbeacons(in:).md)
  Stops the delivery of notifications for the specified beacon region.
- [class func deferredLocationUpdatesAvailable() -> Bool](cllocationmanager/deferredlocationupdatesavailable.md)
  Returns a Boolean value indicating whether the device supports deferred location updates.
- [func allowDeferredLocationUpdates(untilTraveled: CLLocationDistance, timeout: TimeInterval)](cllocationmanager/allowdeferredlocationupdates(untiltraveled:timeout:).md)
  Asks the location manager to defer the delivery of location updates until the specified criteria are met.
- [func disallowDeferredLocationUpdates()](cllocationmanager/disallowdeferredlocationupdates.md)
  Cancels the deferral of location updates for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startrangingbeacons(in:))*