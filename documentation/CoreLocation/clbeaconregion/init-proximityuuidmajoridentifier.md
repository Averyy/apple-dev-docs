# init(proximityUUID:major:identifier:)

**Framework**: Core Location  
**Kind**: init

Creates and returns a region object that targets a beacon with the specified proximity ID and major value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)
```

#### Return Value

An initialized beacon region object.

#### Discussion

This method creates a region that reports all beacons with the specified `proximityUUID` and `major` values. The system ignores the beacon’s [`minor`](clbeaconregion/minor.md) value.

## Parameters

- `proximityUUID`: The unique ID of the beacons you’re targeting. This value can’t be  .
- `major`: The major value that you use to identify one or more beacons.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be  .

## See Also

- [init(proximityUUID: UUID, identifier: String)](clbeaconregion/init(proximityuuid:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:minor:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.
- [var proximityUUID: UUID](clbeaconregion/proximityuuid.md)
  The unique ID of the beacons you’re targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:major:identifier:))*