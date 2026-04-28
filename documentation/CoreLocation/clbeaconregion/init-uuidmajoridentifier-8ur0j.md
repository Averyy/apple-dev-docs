# init(uuid:major:identifier:)

**Framework**: Core Location  
**Kind**: init

Creates and returns a region object that targets beacons with the specified UUID and major value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)
```

## Parameters

- `uuid`: A [`NSUUID`](https://developer.apple.com/documentation/Foundation/NSUUID) that identifies the beacons to target.
- `major`: The [`CLBeaconMajorValue`](clbeaconmajorvalue.md) that characterizes beacons for this region to target.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil.`

## See Also

- [init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)](clbeaconregion/init(beaconidentityconstraint:identifier:).md)
  Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.
- [init(uuid: UUID, identifier: String)](clbeaconregion/init(uuid:identifier:)-6hg8v.md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(uuid:major:minor:identifier:)-24h7w.md)
  Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.
- [typealias CLBeaconMajorValue](clbeaconmajorvalue.md)
  The most significant value in a beacon.
- [typealias CLBeaconMinorValue](clbeaconminorvalue.md)
  The least significant value in a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(uuid:major:identifier:)-8ur0j)*