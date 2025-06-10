# CLRegionState

**Framework**: Core Location  
**Kind**: enum

Constants that reflect the relationship of the current location to the region boundaries.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@frozen
enum CLRegionState
```

## Topics

### Region States
- [CLRegionState.unknown](clregionstate/unknown.md)
  It is unknown whether the location is inside or outside of the region.
- [CLRegionState.inside](clregionstate/inside.md)
  The location is inside of the given region.
- [CLRegionState.outside](clregionstate/outside.md)
  The location is outside of the given region.
### Initializers
- [init?(rawValue: Int)](clregionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didenterregion:).md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didexitregion:).md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:).md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md)
  Tells the delegate that a region monitoring error occurred.
- [func locationManager(CLLocationManager, didStartMonitoringFor: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:).md)
  Tells the delegate that a new region is being monitored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregionstate)*