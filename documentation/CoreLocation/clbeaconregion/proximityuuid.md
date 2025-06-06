# proximityUUID

**Framework**: Core Location  
**Kind**: property

The unique ID of the beacons you’re targeting.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var proximityUUID: UUID { get }
```

#### Discussion

Typically, the UUID is unique to your company and is the same for all of the beacons that you install. Use the [`major`](clbeaconregion/major.md) and [`minor`](clbeaconregion/minor.md) values to differentiate the beacons in your installation.

## See Also

- [init(proximityUUID: UUID, identifier: String)](clbeaconregion/init(proximityuuid:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:minor:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/proximityuuid)*