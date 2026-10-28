# locationManager(_:didDetermineState:for:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about the state of the specified region.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, for region: CLRegion)
```

```objc
- (void) locationManager:(CLLocationManager *) manager didDetermineState:(CLRegionState) state forRegion:(CLRegion *) region;
```

## Discussion

The location manager calls this method whenever there is a boundary transition for a region. It calls this method in addition to calling the  [`locationManager(_:didEnterRegion:)`](./locationmanager%28_,didenterregion%29.md) and [`locationManager(_:didExitRegion:)`](./locationmanager%28_,didexitregion%29.md) methods. The location manager also calls this method in response to a call to its [`requestState(for:)`](../cllocationmanager/requeststate%28for%29.md) method, which runs asynchronously.

## Parameters

- `manager`: The location manager object reporting the event.
- `state`: The state of the specified region. For a list of possible values, see the [`CLRegionState`](../clregionstate.md) type.
- `region`: The region whose state was determined.

## See Also

### Receiving region-related updates
- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](./locationmanager%28_,didenterregion%29.md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](./locationmanager%28_,didexitregion%29.md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](./locationmanager%28_,monitoringdidfailfor,witherror%29.md)
  Tells the delegate that a region monitoring error occurred.
- [func locationManager(CLLocationManager, didStartMonitoringFor: CLRegion)](./locationmanager%28_,didstartmonitoringfor%29.md)
  Tells the delegate that a new region is being monitored.
- [enum CLRegionState](../clregionstate.md)
  Constants that reflect the relationship of the current location to the region boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:))*