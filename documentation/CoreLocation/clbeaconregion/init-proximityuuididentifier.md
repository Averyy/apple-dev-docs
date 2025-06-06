# init(proximityUUID:identifier:)

**Framework**: Core Location  
**Kind**: init

Creates and returns a region object that targets a beacon with the specified UUID.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
init(proximityUUID: UUID, identifier: String)
```

#### Return Value

An initialized beacon region object.

#### Discussion

This method creates a region that results in the reporting of all beacons with the specified `proximityUUID` value. The system ignores the [`major`](clbeaconregion/major.md) and [`minor`](clbeaconregion/minor.md) values of the beacons.

## Parameters

- `proximityUUID`: The unique ID of the beacons you’re targeting. This value can’t be  .
- `identifier`: A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be  .

## See Also

- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:minor:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.
- [var proximityUUID: UUID](clbeaconregion/proximityuuid.md)
  The unique ID of the beacons you’re targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:identifier:))*