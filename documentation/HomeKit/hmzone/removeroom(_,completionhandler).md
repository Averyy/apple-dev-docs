# removeRoom(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a room from the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
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

## Parameters

- `room`: The room to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Assigning Rooms to a Zone
- [var rooms: [HMRoom]](./rooms.md)
  Array of rooms in the zone.
- [func addRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](./addroom%28_,completionhandler%29.md)
  Adds a room to the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/removeroom(_:completionhandler:))*