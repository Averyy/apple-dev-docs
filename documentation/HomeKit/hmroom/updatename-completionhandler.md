# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the name of the room.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateName(_ name: String) async throws
```

## Parameters

- `name`: The new name which must not be  .
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmroom/name.md)
  The name of the room.
- [var uniqueIdentifier: UUID](hmroom/uniqueidentifier.md)
  The unique identifier for a room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmroom/updatename(_:completionhandler:))*