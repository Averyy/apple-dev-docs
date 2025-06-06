# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the name of the service to the specified string.

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

- `name`: The new name. Must not match an existing name in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmservice/name.md)
  The user specified name of the service.
- [var uniqueIdentifier: UUID](hmservice/uniqueidentifier.md)
  A unique identifier for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/updatename(_:completionhandler:))*