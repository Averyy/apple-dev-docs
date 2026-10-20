# addRoom(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Creates a new room with the specified name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addRoom(withName roomName: String, completionHandler completion: @escaping @Sendable (HMRoom?, (any Error)?) -> Void)
```

```swift
func addRoom(named roomName: String) async throws -> HMRoom
```

```objc
- (void) addRoomWithName:(NSString *) roomName completionHandler:(void (^)(HMRoom *room, NSError *error)) completion;
```

## Parameters

- `roomName`: The name of the new room. Must not be `nil`, and must not be the name of a room already in the home.
- `completion`: The block executed after the request is processed.

  - **room**: The newly created room.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Dividing a house into rooms
- [var rooms: [HMRoom]](./rooms.md)
  An array of the rooms created and managed by the user.
- [func roomForEntireHome() -> HMRoom](./roomforentirehome%28%29.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](./removeroom%28_,completionhandler%29.md)
  Removes a room from the home.
- [class HMRoom](../hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addroom(withname:completionhandler:))*