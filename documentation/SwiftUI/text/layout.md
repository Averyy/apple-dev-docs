# Text.Layout

**Framework**: SwiftUI  
**Kind**: struct

A value describing the layout and custom attributes of a tree of `Text` views.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Layout
```

## Topics

### Structures
- [Text.Layout.CharacterIndex](text/layout/characterindex.md)
  The index of a character in the source text. An opaque type, this is intended to be used to determine relative locations of elements in the layout, rather than how they map to the source strings.
- [Text.Layout.DrawingOptions](text/layout/drawingoptions.md)
  Option flags used when drawing `Text.Layout` lines or runs into a graphics context.
- [Text.Layout.Line](text/layout/line.md)
  A single line in a text layout: a collection of runs of placed glyphs.
- [Text.Layout.Run](text/layout/run.md)
  A run of placed glyphs in a text layout.
- [Text.Layout.RunSlice](text/layout/runslice.md)
  A slice of a run of placed glyphs in a text layout.
- [Text.Layout.TypographicBounds](text/layout/typographicbounds.md)
  The typographic bounds of an element in a text layout.
### Instance Properties
- [var isTruncated: Bool](text/layout/istruncated.md)
  Indicates if this text is truncated.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout)*