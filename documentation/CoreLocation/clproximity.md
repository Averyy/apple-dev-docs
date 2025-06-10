# CLProximity

**Framework**: Core Location  
**Kind**: enum

Constants that reflect the relative distance to a beacon.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
enum CLProximity
```

## Topics

### Proximity Values
- [CLProximity.unknown](clproximity/unknown.md)
  The proximity of the beacon could not be determined.
- [CLProximity.immediate](clproximity/immediate.md)
  The beacon is in the user’s immediate vicinity.
- [CLProximity.near](clproximity/near.md)
  The beacon is relatively close to the user.
- [CLProximity.far](clproximity/far.md)
  The beacon is far away.
### Initializers
- [init?(rawValue: Int)](clproximity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var proximity: CLProximity](clbeacon/proximity.md)
  The relative distance to the beacon.
- [var accuracy: CLLocationAccuracy](clbeacon/accuracy.md)
  The accuracy of the proximity value, measured in meters from the beacon.
- [var rssi: Int](clbeacon/rssi.md)
  The received signal strength of the beacon, measured in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clproximity)*