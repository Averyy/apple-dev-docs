# init(proximityUUID:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates and returns a region object that targets a beacon with the specified UUID.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use [`init(uuid:identifier:)`](./init%28uuid,identifier%29-6hg8v.md) instead.

## Declaration

```swift
init(proximityUUID: UUID, identifier: String)
```

```objc
- (instancetype) initWithProximityUUID:(NSUUID *) proximityUUID identifier:(NSString *) identifier;
```

#### Return Value

An initialized beacon region object.

#### Discussion

This method creates a region that results in the reporting of all beacons with the specified `proximityUUID` value. The system ignores the [`major`](./major.md) and [`minor`](./minor.md) values of the beacons.

## Parameters

- `proximityUUID`: The unique ID of the beacons you’re targeting. This value can’t be `nil`.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.

## See Also

### Deprecated
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](./init%28proximityuuid,major,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./init%28proximityuuid,major,minor,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.
- [var proximityUUID: UUID](./proximityuuid.md)
  The unique ID of the beacons you’re targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:identifier:))*