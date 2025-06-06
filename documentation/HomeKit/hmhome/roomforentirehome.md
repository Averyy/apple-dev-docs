# roomForEntireHome()

**Framework**: HomeKit  
**Kind**: method

A room that represents all parts of the home that don’t have a more specific room to represent them.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func roomForEntireHome() -> HMRoom
```

#### Return Value

The room that represents all parts of the home that don’t have a more specific room to represent them.

#### Discussion

HomeKit assigns new accessories to this room until you assign them to a more specific room with [`assignAccessory(_:to:completionHandler:)`](hmhome/assignaccessory(_:to:completionhandler:).md), or until the user assigns them to a room using the Home app.

You can’t rename this room, add it to a zone, or remove it from the home. It also doesn’t appear in the home’s [`rooms`](hmhome/rooms.md) array.

## See Also

- [var rooms: [HMRoom]](hmhome/rooms.md)
  An array of the rooms created and managed by the user.
- [func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)](hmhome/addroom(withname:completionhandler:).md)
  Creates a new room with the specified name.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/removeroom(_:completionhandler:).md)
  Removes a room from the home.
- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/roomforentirehome())*