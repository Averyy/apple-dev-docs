# proximity

**Framework**: Core Location  
**Kind**: property

The relative distance to the beacon.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var proximity: CLProximity { get }
```

#### Discussion

The value in this property gives a general sense of the relative distance to the beacon. Use it to quickly identify beacons that are nearer to the user rather than farther away.

## See Also

- [enum CLProximity](clproximity.md)
  Constants that reflect the relative distance to a beacon.
- [var accuracy: CLLocationAccuracy](clbeacon/accuracy.md)
  The accuracy of the proximity value, measured in meters from the beacon.
- [var rssi: Int](clbeacon/rssi.md)
  The received signal strength of the beacon, measured in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeacon/proximity)*