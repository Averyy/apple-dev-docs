# Transcript.Segment

**Framework**: Foundation Models  
**Kind**: enum

The types of segments that may be included in a transcript entry.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Segment
```

## Topics

### Creating a segment
- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [case structure(Transcript.StructuredSegment)](transcript/segment/structure(_:).md)
  A segment containing structured content
- [case text(Transcript.TextSegment)](transcript/segment/text(_:).md)
  A segment containing text.
### Inspecting a segment
- [var id: String](transcript/segment/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [Transcript.Segment.ID](transcript/segment/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Encoding a segment
- [func encode(to: any Encoder) throws](transcript/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing segments
- [static func == (Transcript.Segment, Transcript.Segment) -> Bool](transcript/segment/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomStringConvertible Implementations](transcript/segment/customstringconvertible-implementations.md)
- [Equatable Implementations](transcript/segment/equatable-implementations.md)

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
- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/segment)*