# init(uuid:major:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates and returns a region object that targets beacons with the specified UUID and major value.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)
```

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid major:(CLBeaconMajorValue) major identifier:(NSString *) identifier;
```

## Parameters

- `uuid`: A [`NSUUID`](../../Foundation/nsuuid.md) that identifies the beacons to target.
- `major`: The [`CLBeaconMajorValue`](../clbeaconmajorvalue.md) that characterizes beacons for this region to target.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil.`

## See Also

### Creating a beacon region
- [init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)](./init%28beaconidentityconstraint,identifier%29.md)
  Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.
- [init(uuid: UUID, identifier: String)](./init%28uuid,identifier%29-6hg8v.md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./init%28uuid,major,minor,identifier%29-24h7w.md)
  Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.
- [typealias CLBeaconMajorValue](../clbeaconmajorvalue.md)
  The most significant value in a beacon.
- [typealias CLBeaconMinorValue](../clbeaconminorvalue.md)
  The least significant value in a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(uuid:major:identifier:)-8ur0j)*