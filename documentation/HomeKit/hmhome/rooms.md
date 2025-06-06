# rooms

**Framework**: HomeKit  
**Kind**: property

An array of the rooms created and managed by the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rooms: [HMRoom] { get }
```

#### Discussion

Each [`HMHome`](hmhome.md) instance has an immutable default room — returned by the [`roomForEntireHome()`](hmhome/roomforentirehome().md) method — to hold accessories that the user hasn’t assigned to a specific room. Unlike user-managed rooms, the default room doesn’t appear in the [`rooms`](hmhome/rooms.md) array.

## See Also

- [func roomForEntireHome() -> HMRoom](hmhome/roomforentirehome.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)](hmhome/addroom(withname:completionhandler:).md)
  Creates a new room with the specified name.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/removeroom(_:completionhandler:).md)
  Removes a room from the home.
- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/rooms)*