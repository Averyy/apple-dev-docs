# locationManager(_:didStartMonitoringFor:)

**Framework**: Core Location  
**Kind**: method

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

## Parameters

- `manager`: The location manager object reporting the event.
- `region`: The region that is being monitored.

## See Also

- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didenterregion:).md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didexitregion:).md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:).md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md)
  Tells the delegate that a region monitoring error occurred.
- [enum CLRegionState](clregionstate.md)
  Constants that reflect the relationship of the current location to the region boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:))*