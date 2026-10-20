# rooms

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSArray<HMRoom *> * rooms;
```

#### Discussion

Each [`HMHome`](../hmhome.md) instance has an immutable default room — returned by the [`roomForEntireHome()`](./roomforentirehome%28%29.md) method — to hold accessories that the user hasn’t assigned to a specific room. Unlike user-managed rooms, the default room doesn’t appear in the [`rooms`](./rooms.md) array.

## See Also

### Dividing a house into rooms
- [func roomForEntireHome() -> HMRoom](./roomforentirehome%28%29.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)](./addroom%28withname,completionhandler%29.md)
  Creates a new room with the specified name.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](./removeroom%28_,completionhandler%29.md)
  Removes a room from the home.
- [class HMRoom](../hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/rooms)*