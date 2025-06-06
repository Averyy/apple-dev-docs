# draw(withFrame:in:characterIndex:layoutManager:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Draws the cell’s image using the specified layout manager.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func draw(withFrame cellFrame: NSRect, in controlView: NSView?, characterIndex charIndex: Int, layoutManager: NSLayoutManager)
```

## Parameters

- `cellFrame`: The frame rectangle in which to draw.
- `controlView`: The view in which to draw.
- `charIndex`: The index of the attachment character within the text.
- `layoutManager`: The layout manager for the text.

## See Also

- [func draw(withFrame: NSRect, in: NSView?)](nstextattachmentcellprotocol/draw(withframe:in:).md)
  Draws the cell’s image in the specified rectangle of the currently focused view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:).md)
  Draws the cell’s image at the specified index point in the view.
- [func highlight(Bool, withFrame: NSRect, in: NSView?)](nstextattachmentcellprotocol/highlight(_:withframe:in:).md)
  Draws the receiver’s image with optional highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/draw(withframe:in:characterindex:layoutmanager:))*