# locationManager(_:didFailRangingFor:error:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didFailRangingFor beaconConstraint: CLBeaconIdentityConstraint, error: any Error)
```

```objc
- (void) locationManager:(CLLocationManager *) manager didFailRangingBeaconsForConstraint:(CLBeaconIdentityConstraint *) beaconConstraint error:(NSError *) error;
```

## Parameters

- `manager`: The [`CLLocationManager`](../cllocationmanager.md) that corresponds to this delegate.
- `beaconConstraint`: The [`CLBeaconIdentityConstraint`](../clbeaconidentityconstraint.md) that describes the characteristics of the beacons the location manager is looking for.
- `error`: An [`NSError`](../../Foundation/nserror.md) object that describes the error.

## See Also

### Receiving beacon-related updates
- [func locationManager(CLLocationManager, didRange: [CLBeacon], satisfying: CLBeaconIdentityConstraint)](./locationmanager%28_,didrange,satisfying%29.md)
  Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [func locationManager(CLLocationManager, didRangeBeacons: [CLBeacon], in: CLBeaconRegion)](./locationmanager%28_,didrangebeacons,in%29.md)
  Tells the delegate that one or more beacons are in range.
- [func locationManager(CLLocationManager, rangingBeaconsDidFailFor: CLBeaconRegion, withError: any Error)](./locationmanager%28_,rangingbeaconsdidfailfor,witherror%29.md)
  Tells the delegate that an error occurred while gathering ranging information for a set of beacons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:))*