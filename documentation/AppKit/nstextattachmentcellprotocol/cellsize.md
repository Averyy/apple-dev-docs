# cellSize()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the size of the attachment’s icon.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func cellSize() -> NSSize
```

## See Also

- [var icon: NSImage? { get set }](../Foundation/FileWrapper/icon.md)
  The icon that represents the file wrapper.
- [var fileWrapper: FileWrapper?](nstextattachment/filewrapper.md)
  The text attachment’s file wrapper.
- [func cellBaselineOffset() -> NSPoint](nstextattachmentcellprotocol/cellbaselineoffset.md)
  Returns the text position where you draw the attachment cell’s image, relative to the current point established in the glyph layout.
- [func cellFrame(for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nstextattachmentcellprotocol/cellframe(for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the frame of the cell to draw at the specified position in a text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/cellsize())*