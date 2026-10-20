# cellSize()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the size of the attachment’s icon.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
func cellSize() -> NSSize
```

```objc
- (NSSize) cellSize;
```

## See Also

### Related Documentation
- [var icon: NSImage?](../../Foundation/filewrapper/icon.md)
  The icon that represents the file wrapper.
- [var fileWrapper: FileWrapper?](../nstextattachment/filewrapper.md)
  The text attachment’s file wrapper.
### Providing the cell metrics
- [func cellBaselineOffset() -> NSPoint](./cellbaselineoffset%28%29.md)
  Returns the text position where you draw the attachment cell’s image, relative to the current point established in the glyph layout.
- [func cellFrame(for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./cellframe%28for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the frame of the cell to draw at the specified position in a text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/cellsize())*