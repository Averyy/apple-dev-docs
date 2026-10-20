# CLRegionState

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CLRegionState : NSInteger;
```

## Topics

### Region States
- [CLRegionState.unknown](./clregionstate/unknown.md)
  It is unknown whether the location is inside or outside of the region.
- [CLRegionState.inside](./clregionstate/inside.md)
  The location is inside of the given region.
- [CLRegionState.outside](./clregionstate/outside.md)
  The location is outside of the given region.
### Initializers
- [init?(rawValue: Int)](./clregionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Receiving region-related updates
- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,didenterregion%29.md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,didexitregion%29.md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,diddeterminestate,for%29.md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](./cllocationmanagerdelegate/locationmanager%28_,monitoringdidfailfor,witherror%29.md)
  Tells the delegate that a region monitoring error occurred.
- [func locationManager(CLLocationManager, didStartMonitoringFor: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,didstartmonitoringfor%29.md)
  Tells the delegate that a new region is being monitored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregionstate)*