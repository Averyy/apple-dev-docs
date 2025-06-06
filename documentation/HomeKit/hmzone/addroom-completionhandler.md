# addRoom(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a room to the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func addRoom(_ room: HMRoom) async throws
```

## Parameters

- `room`: The room to add; must be in the same home as the zone.
- `completion`: The block executed after the request is processed.

## See Also

- [var rooms: [HMRoom]](hmzone/rooms.md)
  Array of rooms in the zone.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmzone/removeroom(_:completionhandler:).md)
  Removes a room from the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/addroom(_:completionhandler:))*