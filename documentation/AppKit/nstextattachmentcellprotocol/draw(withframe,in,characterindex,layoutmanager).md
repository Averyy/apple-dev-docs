# draw(withFrame:in:characterIndex:layoutManager:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Draws the cell’s image using the specified layout manager.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func draw(withFrame cellFrame: NSRect, in controlView: NSView?, characterIndex charIndex: Int, layoutManager: NSLayoutManager)
```

```objc
- (void) drawWithFrame:(NSRect) cellFrame inView:(NSView *) controlView characterIndex:(NSUInteger) charIndex layoutManager:(NSLayoutManager *) layoutManager;
```

## Parameters

- `cellFrame`: The frame rectangle in which to draw.
- `controlView`: The view in which to draw.
- `charIndex`: The index of the attachment character within the text.
- `layoutManager`: The layout manager for the text.

## See Also

### Drawing the cell contents
- [func draw(withFrame: NSRect, in: NSView?)](./draw%28withframe,in%29.md)
  Draws the cell’s image in the specified rectangle of the currently focused view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](./draw%28withframe,in,characterindex%29.md)
  Draws the cell’s image at the specified index point in the view.
- [func highlight(Bool, withFrame: NSRect, in: NSView?)](./highlight%28_,withframe,in%29.md)
  Draws the receiver’s image with optional highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/draw(withframe:in:characterindex:layoutmanager:))*