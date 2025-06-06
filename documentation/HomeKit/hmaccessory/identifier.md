# identifier

**Framework**: HomeKit  
**Kind**: property

A unique identifier for the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var identifier: UUID { get }
```

#### Discussion

An identifier is stable for as long as an accessory is in a home. If an accessory is removed from a home, it will get a new identifier when it is next added to a home.

## See Also

- [var name: String](hmaccessory/name.md)
  The name of the accessory.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmaccessory/updatename(_:completionhandler:).md)
  Changes the name of the accessory.
- [var uniqueIdentifier: UUID](hmaccessory/uniqueidentifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/identifier)*