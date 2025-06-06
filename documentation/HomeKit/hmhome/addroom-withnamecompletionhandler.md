# addRoom(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Creates a new room with the specified name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addRoom(named roomName: String) async throws -> HMRoom
```

## Parameters

- `roomName`: The name of the new room. Must not be  , and must not be the name of a room already in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var rooms: [HMRoom]](hmhome/rooms.md)
  An array of the rooms created and managed by the user.
- [func roomForEntireHome() -> HMRoom](hmhome/roomforentirehome.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/removeroom(_:completionhandler:).md)
  Removes a room from the home.
- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addroom(withname:completionhandler:))*