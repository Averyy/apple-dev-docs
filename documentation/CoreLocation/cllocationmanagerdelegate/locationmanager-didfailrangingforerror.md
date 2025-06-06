# locationManager(_:didFailRangingFor:error:)

**Framework**: Core Location  
**Kind**: method

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

## Parameters

- `manager`: The   that corresponds to this delegate.
- `beaconConstraint`: The   that describes the characteristics of the beacons the location manager is looking for.
- `error`: An   object that describes the error.

## See Also

- [func locationManager(CLLocationManager, didRange: [CLBeacon], satisfying: CLBeaconIdentityConstraint)](cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:).md)
  Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [func locationManager(CLLocationManager, didRangeBeacons: [CLBeacon], in: CLBeaconRegion)](cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:).md)
  Tells the delegate that one or more beacons are in range.
- [func locationManager(CLLocationManager, rangingBeaconsDidFailFor: CLBeaconRegion, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:).md)
  Tells the delegate that an error occurred while gathering ranging information for a set of beacons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:))*