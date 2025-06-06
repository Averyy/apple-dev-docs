# locationManager(_:didRangeBeacons:in:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that one or more beacons are in range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion)
```

## Mentions

- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)

#### Discussion

The location manager calls this method when a new set of beacons becomes available in the specified region or when a beacon goes out of range. The location manager also calls this method when the range of a beacon changes; for example, when a beacon gets closer.

## Parameters

- `manager`: The location manager object reporting the event.
- `beacons`: An array of   objects representing the beacons currently in range. If   is empty, you can assume that no beacons matching the specified region are in range. When a specific beacon is no longer in  , that beacon is no longer received by the device. You can use the information in the   objects to determine the range of each beacon and its identifying information.
- `region`: The region object containing the parameters that were used to locate the beacons.

## See Also

- [func locationManager(CLLocationManager, didRange: [CLBeacon], satisfying: CLBeaconIdentityConstraint)](cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:).md)
  Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [func locationManager(CLLocationManager, didFailRangingFor: CLBeaconIdentityConstraint, error: any Error)](cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:).md)
  Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [func locationManager(CLLocationManager, rangingBeaconsDidFailFor: CLBeaconRegion, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:).md)
  Tells the delegate that an error occurred while gathering ranging information for a set of beacons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:))*