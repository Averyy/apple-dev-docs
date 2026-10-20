# init(proximityUUID:major:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates and returns a region object that targets a beacon with the specified proximity ID and major value.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use [`init(uuid:major:identifier:)`](./init%28uuid,major,identifier%29-8ur0j.md) instead.

## Declaration

```swift
init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)
```

```objc
- (instancetype) initWithProximityUUID:(NSUUID *) proximityUUID major:(CLBeaconMajorValue) major identifier:(NSString *) identifier;
```

#### Return Value

An initialized beacon region object.

#### Discussion

This method creates a region that reports all beacons with the specified `proximityUUID` and `major` values. The system ignores the beacon’s [`minor`](./minor.md) value.

## Parameters

- `proximityUUID`: The unique ID of the beacons you’re targeting. This value can’t be `nil`.
- `major`: The major value that you use to identify one or more beacons.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.

## See Also

### Deprecated
- [init(proximityUUID: UUID, identifier: String)](./init%28proximityuuid,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./init%28proximityuuid,major,minor,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.
- [var proximityUUID: UUID](./proximityuuid.md)
  The unique ID of the beacons you’re targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:major:identifier:))*