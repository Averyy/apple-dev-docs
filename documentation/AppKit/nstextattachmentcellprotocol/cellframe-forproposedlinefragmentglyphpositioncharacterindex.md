# cellFrame(for:proposedLineFragment:glyphPosition:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the frame of the cell to draw at the specified position in a text container.

**Availability**:
- macOS 10.0+

## Declaration

```swift
nonisolated
func cellFrame(for textContainer: NSTextContainer, proposedLineFragment lineFrag: NSRect, glyphPosition position: NSPoint, characterIndex charIndex: Int) -> NSRect
```

#### Discussion

The proposed line fragment is specified by `lineFrag`.

## Parameters

- `textContainer`: The text container that contains the glyph.
- `lineFrag`: The line fragment that contains the glyph.
- `position`: The position of the glyph in the text container.
- `charIndex`: The index of the character.

## See Also

- [func cellSize() -> NSSize](nstextattachmentcellprotocol/cellsize.md)
  Returns the size of the attachment’s icon.
- [func cellBaselineOffset() -> NSPoint](nstextattachmentcellprotocol/cellbaselineoffset.md)
  Returns the text position where you draw the attachment cell’s image, relative to the current point established in the glyph layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/cellframe(for:proposedlinefragment:glyphposition:characterindex:))*