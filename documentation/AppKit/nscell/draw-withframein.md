# draw(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the receiver’s border and then draws the interior of the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func draw(withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

This method draws the cell in the currently focused view, which can be different from the `controlView` passed in. Taking advantage of this behavior is not recommended, however.

## Parameters

- `cellFrame`: The bounding rectangle of the receiver.
- `controlView`: The control that manages the cell.

## See Also

- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](nscell/highlightcolor(withframe:in:).md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](nscell/drawinterior(withframe:in:).md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [var controlView: NSView?](nscell/controlview.md)
  The view associated with the cell.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](nscell/highlight(_:withframe:in:).md)
  Redraws the receiver with the specified highlight setting.
- [var isHighlighted: Bool](nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/draw(withframe:in:))*