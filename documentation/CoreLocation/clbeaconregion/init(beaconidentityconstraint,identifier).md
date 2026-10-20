# init(beaconIdentityConstraint:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)
```

```objc
- (instancetype) initWithBeaconIdentityConstraint:(CLBeaconIdentityConstraint *) beaconIdentityConstraint identifier:(NSString *) identifier;
```

## Parameters

- `beaconIdentityConstraint`: A [`CLBeaconIdentityConstraint`](../clbeaconidentityconstraint.md) that describes the characteristics of beacons for the framework to target.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.

## See Also

### Creating a beacon region
- [init(uuid: UUID, identifier: String)](./init%28uuid,identifier%29-6hg8v.md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)](./init%28uuid,major,identifier%29-8ur0j.md)
  Creates and returns a region object that targets beacons with the specified UUID and major value.
- [init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./init%28uuid,major,minor,identifier%29-24h7w.md)
  Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.
- [typealias CLBeaconMajorValue](../clbeaconmajorvalue.md)
  The most significant value in a beacon.
- [typealias CLBeaconMinorValue](../clbeaconminorvalue.md)
  The least significant value in a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(beaconidentityconstraint:identifier:))*