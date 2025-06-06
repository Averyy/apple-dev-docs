# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the name of the action set.

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

- `name`: The new name; must not be  .
- `completion`: The block executed after the request is processed.

## See Also

- [var uniqueIdentifier: UUID](hmactionset/uniqueidentifier.md)
  The action set’s unique identifier.
- [var name: String](hmactionset/name.md)
  The name of the action set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/updatename(_:completionhandler:))*