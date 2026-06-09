# Transcript.Segment

**Framework**: Foundation Models  
**Kind**: enum

The types of segments that may be included in a transcript entry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Segment
```

## Topics

### Segment cases
- [case text(Transcript.TextSegment)](transcript/segment/text(_:).md)
  A segment containing text.
- [case attachment(Transcript.AttachmentSegment)](transcript/segment/attachment(_:).md)
  A segment containing an attachment.
- [case structure(Transcript.StructuredSegment)](transcript/segment/structure(_:).md)
  A segment containing structured content.
- [case custom(any Transcript.CustomSegment)](transcript/segment/custom(_:).md)
  A segment containing custom content.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(entries: some Sequence<Transcript.Entry>)](transcript/init(entries:).md)
  Creates a transcript.
- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.
- [Transcript.Attachment](transcript/attachment.md)
  The types of attached content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/segment)*