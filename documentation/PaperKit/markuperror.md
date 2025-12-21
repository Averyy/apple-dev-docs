# MarkupError

**Framework**: PaperKit  
**Kind**: enum

The error thrown for encoding / decoding data models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MarkupError
```

## Topics

### Enumeration Cases
- [MarkupError.incompatibleFormatTooNew](markuperror/incompatibleformattoonew.md)
  The data being decoded has a newer format that cannot be decoded.
- [MarkupError.incorrectFormat](markuperror/incorrectformat.md)
  Incorrect format or header.
- [MarkupError.malformedData](markuperror/malformeddata.md)
  The binary data was malformed in some way.

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