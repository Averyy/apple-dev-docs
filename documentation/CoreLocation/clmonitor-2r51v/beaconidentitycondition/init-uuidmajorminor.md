# init(uuid:major:minor:)

**Framework**: Core Location  
**Kind**: init

Creates a beacon identity condition with UUID, and major and minor characteristics.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
init(uuid: UUID, major: UInt16, minor: UInt16)
```

## Parameters

- `uuid`: The  doc://com.apple.documentation/documentation/foundation/nsuuid/1574571-uuid  that identifies the beacon.
- `major`: The   that represents the beacon’s major value.
- `minor`: The   that represents the beacon’s minor value.

## See Also

- [init(uuid: UUID)](clmonitor-2r51v/beaconidentitycondition/init(uuid:).md)
  Creates a beacon identity condition with the UUID characteristic only, and wildcard values for the major and minor characteristics.
- [init(uuid: UUID, major: UInt16)](clmonitor-2r51v/beaconidentitycondition/init(uuid:major:).md)
  Creates a beacon identity condition with UUID and major characteristics, and a wildcard for the minor characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition/init(uuid:major:minor:))*