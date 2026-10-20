# highlight(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Draws the receiver’s image with optional highlighting.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func highlight(_ flag: Bool, withFrame cellFrame: NSRect, in controlView: NSView?)
```

```objc
- (void) highlight:(BOOL) flag withFrame:(NSRect) cellFrame inView:(NSView *) controlView;
```

## Parameters

- `flag`: A Boolean value that indicates whether to highlight the image. Add a highlight if the value is [`true`](../../Swift/true.md).
- `cellFrame`: The frame rectangle in which to draw.
- `controlView`: The view in which to draw.

## See Also

### Related Documentation
- [func highlight(Bool, withFrame: NSRect, in: NSView)](../nscell/highlight%28_,withframe,in%29.md)
  Redraws the receiver with the specified highlight setting.
- [func lockFocus()](../nsview/lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
### Drawing the cell contents
- [func draw(withFrame: NSRect, in: NSView?)](./draw%28withframe,in%29.md)
  Draws the cell’s image in the specified rectangle of the currently focused view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](./draw%28withframe,in,characterindex%29.md)
  Draws the cell’s image at the specified index point in the view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int, layoutManager: NSLayoutManager)](./draw%28withframe,in,characterindex,layoutmanager%29.md)
  Draws the cell’s image using the specified layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/highlight(_:withframe:in:))*