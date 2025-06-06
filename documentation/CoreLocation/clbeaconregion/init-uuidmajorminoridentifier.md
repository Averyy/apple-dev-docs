# init(uuid:major:minor:identifier:)

**Framework**: Core Location  
**Kind**: init

Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)
```

## Parameters

- `uuid`: A  doc://com.apple.documentation/documentation/foundation/nsuuid/1574571-uuid  that identifies the beacons to target.
- `major`: The   that characterizes beacons for this region to target.
- `minor`: The   that characterizes beacons for this region to target.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be 

## See Also

- [init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)](clbeaconregion/init(beaconidentityconstraint:identifier:).md)
  Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.
- [init(uuid: UUID, identifier: String)](clbeaconregion/init(uuid:identifier:).md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(uuid:major:identifier:).md)
  Creates and returns a region object that targets beacons with the specified UUID and major value.
- [typealias CLBeaconMajorValue](clbeaconmajorvalue.md)
  The most significant value in a beacon.
- [typealias CLBeaconMinorValue](clbeaconminorvalue.md)
  The least significant value in a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(uuid:major:minor:identifier:))*