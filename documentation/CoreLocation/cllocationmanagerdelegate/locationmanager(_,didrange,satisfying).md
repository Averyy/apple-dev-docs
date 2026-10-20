# locationManager(_:didRange:satisfying:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didRange beacons: [CLBeacon], satisfying beaconConstraint: CLBeaconIdentityConstraint)
```

```objc
- (void) locationManager:(CLLocationManager *) manager didRangeBeacons:(NSArray<CLBeacon *> *) beacons satisfyingConstraint:(CLBeaconIdentityConstraint *) beaconConstraint;
```

## Parameters

- `manager`: The [`CLLocationManager`](../cllocationmanager.md) that corresponds to this delegate.
- `beacons`: An array of [`CLBeacon`](../clbeacon.md) objects.
- `beaconConstraint`: The [`CLBeaconIdentityConstraint`](../clbeaconidentityconstraint.md) that describes the characteristics of the beacons the location manager is looking for.

## See Also

### Receiving beacon-related updates
- [func locationManager(CLLocationManager, didFailRangingFor: CLBeaconIdentityConstraint, error: any Error)](./locationmanager%28_,didfailrangingfor,error%29.md)
  Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [func locationManager(CLLocationManager, didRangeBeacons: [CLBeacon], in: CLBeaconRegion)](./locationmanager%28_,didrangebeacons,in%29.md)
  Tells the delegate that one or more beacons are in range.
- [func locationManager(CLLocationManager, rangingBeaconsDidFailFor: CLBeaconRegion, withError: any Error)](./locationmanager%28_,rangingbeaconsdidfailfor,witherror%29.md)
  Tells the delegate that an error occurred while gathering ranging information for a set of beacons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:))*