# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the name of the zone.

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

- `name`: The new name. Must not be  ; must be unique within the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmzone/name.md)
  The name of the zone.
- [var uniqueIdentifier: UUID](hmzone/uniqueidentifier.md)
  The unique identifier for a zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/updatename(_:completionhandler:))*