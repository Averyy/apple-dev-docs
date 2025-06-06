# init(proximityUUID:major:minor:identifier:)

**Framework**: Core Location  
**Kind**: init

Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)
```

#### Return Value

An initialized beacon region object.

#### Discussion

This method creates a region that reports the beacon with the specified `proximityUUID`, `major`, and `minor` values.

## Parameters

- `proximityUUID`: The proximity ID of the beacon you’re targeting. This value can’t be  .
- `major`: The major value that you use to identify one or more beacons.
- `minor`: The minor value that you use to identify a specific beacon.
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be  .

## See Also

- [init(proximityUUID: UUID, identifier: String)](clbeaconregion/init(proximityuuid:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [var proximityUUID: UUID](clbeaconregion/proximityuuid.md)
  The unique ID of the beacons you’re targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:major:minor:identifier:))*