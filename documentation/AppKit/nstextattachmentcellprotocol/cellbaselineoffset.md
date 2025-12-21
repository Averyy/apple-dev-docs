# cellBaselineOffset()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the text position where you draw the attachment cell’s image, relative to the current point established in the glyph layout.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func cellBaselineOffset() -> NSPoint
```

#### Discussion

The image should be drawn so its lower-left corner lies on this point.

## See Also

- [var icon: NSImage?](../Foundation/FileWrapper/icon.md)
  The icon that represents the file wrapper.
- [func cellSize() -> NSSize](nstextattachmentcellprotocol/cellsize.md)
  Returns the size of the attachment’s icon.
- [func cellFrame(for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nstextattachmentcellprotocol/cellframe(for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the frame of the cell to draw at the specified position in a text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/cellbaselineoffset())*