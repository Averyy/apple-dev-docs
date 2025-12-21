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

## Declaration

```swift
enum Segment
```

## Topics

### Creating a segment
- [case structure(Transcript.StructuredSegment)](transcript/segment/structure(_:).md)
  A segment containing structured content.
- [case text(Transcript.TextSegment)](transcript/segment/text(_:).md)
  A segment containing text.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(entries: some Sequence<Transcript.Entry>)](transcript/init(entries:).md)
  Creates a transcript.
- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/segment)*