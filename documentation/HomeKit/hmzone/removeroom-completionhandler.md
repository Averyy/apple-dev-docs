# removeRoom(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a room from the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeRoom(_ room: HMRoom) async throws
```

## Parameters

- `room`: The room to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var rooms: [HMRoom]](hmzone/rooms.md)
  Array of rooms in the zone.
- [func addRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmzone/addroom(_:completionhandler:).md)
  Adds a room to the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/removeroom(_:completionhandler:))*