# locationManager(_:didEnterRegion:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that the user entered the specified region.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion)
```

## Mentions

- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)

#### Discussion

Because regions are a shared application resource, every active location manager object delivers this message to its associated delegate. It doesn’t matter which location manager actually registered the specified region. If multiple location managers share a delegate object, that delegate receives the message multiple times.

The region object provided may not be the same one that was registered. As a result, you should never perform pointer-level comparisons to determine equality. Instead, use the region’s identifier string to determine if your delegate should respond.

## Parameters

- `manager`: The location manager object reporting the event.
- `region`: An object containing information about the region that was entered.

## See Also

- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didexitregion:).md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:).md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md)
  Tells the delegate that a region monitoring error occurred.
- [func locationManager(CLLocationManager, didStartMonitoringFor: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:).md)
  Tells the delegate that a new region is being monitored.
- [enum CLRegionState](clregionstate.md)
  Constants that reflect the relationship of the current location to the region boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didenterregion:))*