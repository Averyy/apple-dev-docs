# NSTextSelectionNavigation.Destination.paragraph

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case paragraph
```

```c
NSTextSelectionNavigationDestinationParagraph
```

## See Also

### Selection destinations
- [NSTextSelectionNavigation.Destination.character](./character.md)
  The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigation.Destination.word](./word.md)
  The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigation.Destination.line](./line.md)
  The selection moves to the next line boundary.
- [NSTextSelectionNavigation.Destination.sentence](./sentence.md)
  The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigation.Destination.container](./container.md)
  The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigation.Destination.document](./document.md)
  The selection moves to the document boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/destination/paragraph)*