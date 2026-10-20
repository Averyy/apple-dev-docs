# MarkupError

**Framework**: PaperKit  
**Kind**: enum  
**Role**: Enumeration

The error thrown for encoding / decoding data models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MarkupError
```

## Topics

### Handling error cases
- [MarkupError.incorrectFormat](./markuperror/incorrectformat.md)
  Incorrect format or header.
- [MarkupError.malformedData](./markuperror/malformeddata.md)
  The binary data was malformed in some way.
- [MarkupError.incompatibleFormatTooNew](./markuperror/incompatibleformattoonew.md)
  The data being decoded has a newer format that cannot be decoded.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuperror)*