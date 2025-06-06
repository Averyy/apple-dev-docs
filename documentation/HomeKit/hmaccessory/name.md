# name

**Framework**: HomeKit  
**Kind**: property

The name of the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

Use the [`updateName(_:completionHandler:)`](hmaccessory/updatename(_:completionhandler:).md) method to change the name to a value chosen by the user.

## See Also

- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmaccessory/updatename(_:completionhandler:).md)
  Changes the name of the accessory.
- [var uniqueIdentifier: UUID](hmaccessory/uniqueidentifier.md)
  A unique identifier for the accessory.
- [var identifier: UUID](hmaccessory/identifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/name)*