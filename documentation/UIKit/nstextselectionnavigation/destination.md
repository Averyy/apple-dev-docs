# NSTextSelectionNavigation.Destination

**Framework**: UIKit  
**Kind**: enum

Values that affect how the framework handles navigation across different textual boundaries during a selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Destination
```

## Topics

### Selection destinations
- [NSTextSelectionNavigation.Destination.character](nstextselectionnavigation/destination/character.md)
  The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigation.Destination.word](nstextselectionnavigation/destination/word.md)
  The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigation.Destination.line](nstextselectionnavigation/destination/line.md)
  The selection moves to the next line boundary.
- [NSTextSelectionNavigation.Destination.sentence](nstextselectionnavigation/destination/sentence.md)
  The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigation.Destination.paragraph](nstextselectionnavigation/destination/paragraph.md)
  The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigation.Destination.container](nstextselectionnavigation/destination/container.md)
  The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigation.Destination.document](nstextselectionnavigation/destination/document.md)
  The selection moves to the document boundary.
### Initializers
- [init?(rawValue: Int)](nstextselectionnavigation/destination/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var allowsNonContiguousRanges: Bool](nstextselectionnavigation/allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Direction](nstextselectionnavigation/direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](nstextselectionnavigation/textselection(for:enclosing:incontainerat:).md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination)*