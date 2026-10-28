# init(proximityUUID:major:minor:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use [`init(uuid:major:minor:identifier:)`](./init%28uuid,major,minor,identifier%29-24h7w.md) instead.

## Declaration

```swift
init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)
```

```objc
- (instancetype) initWithProximityUUID:(NSUUID *) proximityUUID major:(CLBeaconMajorValue) major minor:(CLBeaconMinorValue) minor identifier:(NSString *) identifier;
```

## Return Value

An initialized beacon region object.

## Discussion

This method creates a region that reports the beacon with the specified `proximityUUID`, `major`, and `minor` values.

## Parameters

- `proximityUUID`: The proximity ID of the beacon you’re targeting. This value can’t be `nil`.
- `major`: The major value that you use to identify one or more beacons.
- `minor`: The minor value that you use to identify a specific beacon.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.

## See Also

### Deprecated
- [init(proximityUUID: UUID, identifier: String)](./init%28proximityuuid,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](./init%28proximityuuid,major,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [var proximityUUID: UUID](./proximityuuid.md)
  The unique ID of the beacons you’re targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:major:minor:identifier:))*