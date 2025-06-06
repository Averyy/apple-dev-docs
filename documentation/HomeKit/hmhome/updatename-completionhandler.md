# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the name of the home.

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

- `name`: The new name. Must not already exist in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmhome/name.md)
  The name the user gives to the home.
- [var uniqueIdentifier: UUID](hmhome/uniqueidentifier.md)
  A unique identifier for the home.
- [var isPrimary: Bool](hmhome/isprimary.md)
  A Boolean value that indicates whether this is the primary home for its home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/updatename(_:completionhandler:))*