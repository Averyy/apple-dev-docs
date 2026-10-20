# addRoom(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a room to the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func addRoom(_ room: HMRoom, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func addRoom(_ room: HMRoom) async throws
```

```objc
- (void) addRoom:(HMRoom *) room completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `room`: The room to add; must be in the same home as the zone.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Assigning Rooms to a Zone
- [var rooms: [HMRoom]](./rooms.md)
  Array of rooms in the zone.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](./removeroom%28_,completionhandler%29.md)
  Removes a room from the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/addroom(_:completionhandler:))*