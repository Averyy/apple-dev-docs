# NSTextSelectionNavigation.Destination.line

**Framework**: AppKit  
**Kind**: case

The selection moves to the next line boundary.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case line
```

#### Discussion

The boundary of a line can be logical, based on the line separator characters, as well as visual using soft line wrapping.

## See Also

- [NSTextSelectionNavigation.Destination.character](nstextselectionnavigation/destination/character.md)
  The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigation.Destination.word](nstextselectionnavigation/destination/word.md)
  The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigation.Destination.sentence](nstextselectionnavigation/destination/sentence.md)
  The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigation.Destination.paragraph](nstextselectionnavigation/destination/paragraph.md)
  The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigation.Destination.container](nstextselectionnavigation/destination/container.md)
  The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigation.Destination.document](nstextselectionnavigation/destination/document.md)
  The selection moves to the document boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/destination/line)*