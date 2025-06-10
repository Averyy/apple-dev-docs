# MarkupError

**Framework**: PaperKit  
**Kind**: enum

The error thrown for encoding / decoding data models.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum MarkupError
```

## Topics

### Operators
- [static func == (MarkupError, MarkupError) -> Bool](markuperror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MarkupError.incompatibleFormatTooNew](markuperror/incompatibleformattoonew.md)
  The data being decoded has a newer format that cannot be decoded.
- [MarkupError.incorrectFormat](markuperror/incorrectformat.md)
  Incorrect format or header.
- [MarkupError.malformedData](markuperror/malformeddata.md)
  The binary data was malformed in some way.
### Instance Properties
- [var hashValue: Int](markuperror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](markuperror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](markuperror/equatable-implementations.md)
- [Error Implementations](markuperror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuperror)*