# removeRoom(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a room from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeRoom(_ room: HMRoom, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeRoom(_ room: HMRoom) async throws
```

```objc
- (void) removeRoom:(HMRoom *) room completionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

If the room is in a zone, this method also removes it from the zone. Any accessories in the removed room automatically move to [`roomForEntireHome()`](./roomforentirehome%28%29.md).

## Parameters

- `room`: The room to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Dividing a house into rooms
- [var rooms: [HMRoom]](./rooms.md)
  An array of the rooms created and managed by the user.
- [func roomForEntireHome() -> HMRoom](./roomforentirehome%28%29.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)](./addroom%28withname,completionhandler%29.md)
  Creates a new room with the specified name.
- [class HMRoom](../hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeroom(_:completionhandler:))*