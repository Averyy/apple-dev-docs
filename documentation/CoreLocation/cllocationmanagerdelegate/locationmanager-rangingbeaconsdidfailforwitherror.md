# locationManager(_:rangingBeaconsDidFailFor:withError:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that an error occurred while gathering ranging information for a set of beacons.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, rangingBeaconsDidFailFor region: CLBeaconRegion, withError error: any Error)
```

#### Discussion

Errors occur most often when registering a beacon region failed. If the region object itself is invalid or if it contains invalid data, the location manager calls this method to report the problem.

## Parameters

- `manager`: The location manager object reporting the event.
- `region`: The region object that encountered the error.
- `error`: An error object containing the error code that indicates why ranging failed.

## See Also

- [func locationManager(CLLocationManager, didRange: [CLBeacon], satisfying: CLBeaconIdentityConstraint)](cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:).md)
  Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [func locationManager(CLLocationManager, didFailRangingFor: CLBeaconIdentityConstraint, error: any Error)](cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:).md)
  Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [func locationManager(CLLocationManager, didRangeBeacons: [CLBeacon], in: CLBeaconRegion)](cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:).md)
  Tells the delegate that one or more beacons are in range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:))*