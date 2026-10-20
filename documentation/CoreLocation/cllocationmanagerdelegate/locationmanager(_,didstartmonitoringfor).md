# locationManager(_:didStartMonitoringFor:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a new region is being monitored.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didStartMonitoringFor region: CLRegion)
```

```objc
- (void) locationManager:(CLLocationManager *) manager didStartMonitoringForRegion:(CLRegion *) region;
```

## Parameters

- `manager`: The location manager object reporting the event.
- `region`: The region that is being monitored.

## See Also

### Receiving region-related updates
- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](./locationmanager%28_,didenterregion%29.md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](./locationmanager%28_,didexitregion%29.md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](./locationmanager%28_,diddeterminestate,for%29.md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](./locationmanager%28_,monitoringdidfailfor,witherror%29.md)
  Tells the delegate that a region monitoring error occurred.
- [enum CLRegionState](../clregionstate.md)
  Constants that reflect the relationship of the current location to the region boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:))*