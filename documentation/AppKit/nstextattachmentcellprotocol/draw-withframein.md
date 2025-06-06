# draw(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Draws the cell’s image in the specified rectangle of the currently focused view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func draw(withFrame cellFrame: NSRect, in controlView: NSView?)
```

## Parameters

- `cellFrame`: The frame rectangle in which to draw.
- `controlView`: The view in which to draw.

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [Text Attachment Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttachments/TextAttachments.html#//apple_ref/doc/uid/10000094i)
- [func lockFocus()](nsview/lockfocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:).md)
  Draws the cell’s image at the specified index point in the view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int, layoutManager: NSLayoutManager)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:layoutmanager:).md)
  Draws the cell’s image using the specified layout manager.
- [func highlight(Bool, withFrame: NSRect, in: NSView?)](nstextattachmentcellprotocol/highlight(_:withframe:in:).md)
  Draws the receiver’s image with optional highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/draw(withframe:in:))*