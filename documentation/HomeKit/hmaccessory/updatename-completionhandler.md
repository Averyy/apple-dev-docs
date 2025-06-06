# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Changes the name of the accessory.

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

- `name`: The new name.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmaccessory/name.md)
  The name of the accessory.
- [var uniqueIdentifier: UUID](hmaccessory/uniqueidentifier.md)
  A unique identifier for the accessory.
- [var identifier: UUID](hmaccessory/identifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/updatename(_:completionhandler:))*