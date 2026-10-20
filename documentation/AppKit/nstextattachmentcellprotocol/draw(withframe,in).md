# draw(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Draws the cell’s image in the specified rectangle of the currently focused view.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func draw(withFrame cellFrame: NSRect, in controlView: NSView?)
```

```objc
- (void) drawWithFrame:(NSRect) cellFrame inView:(NSView *) controlView;
```

## Parameters

- `cellFrame`: The frame rectangle in which to draw.
- `controlView`: The view in which to draw.

## See Also

### Related Documentation
- [func draw(withFrame: NSRect, in: NSView)](../nscell/draw%28withframe,in%29.md)
  Draws the receiver’s border and then draws the interior of the cell.
- [Text Attachment Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttachments/TextAttachments.html#//apple_ref/doc/uid/10000094i)
- [func lockFocus()](../nsview/lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
### Drawing the cell contents
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](./draw%28withframe,in,characterindex%29.md)
  Draws the cell’s image at the specified index point in the view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int, layoutManager: NSLayoutManager)](./draw%28withframe,in,characterindex,layoutmanager%29.md)
  Draws the cell’s image using the specified layout manager.
- [func highlight(Bool, withFrame: NSRect, in: NSView?)](./highlight%28_,withframe,in%29.md)
  Draws the receiver’s image with optional highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/draw(withframe:in:))*