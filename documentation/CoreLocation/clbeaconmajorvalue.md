# CLBeaconMajorValue

**Framework**: Core Location  
**Kind**: typealias

The most significant value in a beacon.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias CLBeaconMajorValue = UInt16
```

## See Also

- [init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)](clbeaconregion/init(beaconidentityconstraint:identifier:).md)
  Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.
- [init(uuid: UUID, identifier: String)](clbeaconregion/init(uuid:identifier:)-6hg8v.md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(uuid:major:identifier:)-8ur0j.md)
  Creates and returns a region object that targets beacons with the specified UUID and major value.
- [init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(uuid:major:minor:identifier:)-24h7w.md)
  Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.
- [typealias CLBeaconMinorValue](clbeaconminorvalue.md)
  The least significant value in a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconmajorvalue)*