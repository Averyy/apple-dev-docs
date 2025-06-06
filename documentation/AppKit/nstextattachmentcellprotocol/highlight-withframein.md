# highlight(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Draws the receiver’s image with optional highlighting.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlight(_ flag: Bool, withFrame cellFrame: NSRect, in controlView: NSView?)
```

## Parameters

- `flag`: A Boolean value that indicates whether to highlight the image. Add a highlight if the value is  .
- `cellFrame`: The frame rectangle in which to draw.
- `controlView`: The view in which to draw.

## See Also

- [func highlight(Bool, withFrame: NSRect, in: NSView)](nscell/highlight(_:withframe:in:).md)
  Redraws the receiver with the specified highlight setting.
- [func lockFocus()](nsview/lockfocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func draw(withFrame: NSRect, in: NSView?)](nstextattachmentcellprotocol/draw(withframe:in:).md)
  Draws the cell’s image in the specified rectangle of the currently focused view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:).md)
  Draws the cell’s image at the specified index point in the view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int, layoutManager: NSLayoutManager)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:layoutmanager:).md)
  Draws the cell’s image using the specified layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/highlight(_:withframe:in:))*