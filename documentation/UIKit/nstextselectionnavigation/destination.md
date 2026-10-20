# NSTextSelectionNavigation.Destination

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSTextSelectionNavigationDestination : NSInteger;
```

## Topics

### Selection destinations
- [NSTextSelectionNavigation.Destination.character](./destination/character.md)
  The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigation.Destination.word](./destination/word.md)
  The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigation.Destination.line](./destination/line.md)
  The selection moves to the next line boundary.
- [NSTextSelectionNavigation.Destination.sentence](./destination/sentence.md)
  The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigation.Destination.paragraph](./destination/paragraph.md)
  The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigation.Destination.container](./destination/container.md)
  The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigation.Destination.document](./destination/document.md)
  The selection moves to the document boundary.
### Initializers
- [init?(rawValue: Int)](./destination/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selection characteristics
- [var allowsNonContiguousRanges: Bool](./allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](./rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](./modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Direction](./direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](./textselection%28for,enclosing,incontainerat%29.md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination)*