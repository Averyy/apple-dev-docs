# cellBaselineOffset()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text position where you draw the attachment cell’s image, relative to the current point established in the glyph layout.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
func cellBaselineOffset() -> NSPoint
```

```objc
- (NSPoint) cellBaselineOffset;
```

#### Discussion

The image should be drawn so its lower-left corner lies on this point.

## See Also

### Related Documentation
- [var icon: NSImage?](../../Foundation/filewrapper/icon.md)
  The icon that represents the file wrapper.
### Providing the cell metrics
- [func cellSize() -> NSSize](./cellsize%28%29.md)
  Returns the size of the attachment’s icon.
- [func cellFrame(for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./cellframe%28for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the frame of the cell to draw at the specified position in a text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/cellbaselineoffset())*