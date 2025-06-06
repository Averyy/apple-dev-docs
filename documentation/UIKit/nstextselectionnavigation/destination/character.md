# NSTextSelectionNavigation.Destination.character

**Framework**: UIKit  
**Kind**: case

The selection moves to the next extended grapheme cluster boundary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case character
```

#### Discussion

When the movement direction isn’t along the line (for example up and down for a horizontal line), it moves to the adjacent line using the anchor point instead of resolving to the logical direction. This could result in a location inside a cluster depending on the specific characteristics of a given script.  For example, certain Indic scripts combine characters in specific ways depending on usage and position to form composite characters. The framework returns a location consistent with the rules of the script and the direction of movement.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination/character)*