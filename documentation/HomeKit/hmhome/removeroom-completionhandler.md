# removeRoom(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a room from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeRoom(_ room: HMRoom) async throws
```

#### Discussion

If the room is in a zone, this method also removes it from the zone. Any accessories in the removed room automatically move to [`roomForEntireHome()`](hmhome/roomforentirehome().md).

## Parameters

- `room`: The room to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var rooms: [HMRoom]](hmhome/rooms.md)
  An array of the rooms created and managed by the user.
- [func roomForEntireHome() -> HMRoom](hmhome/roomforentirehome.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)](hmhome/addroom(withname:completionhandler:).md)
  Creates a new room with the specified name.
- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeroom(_:completionhandler:))*