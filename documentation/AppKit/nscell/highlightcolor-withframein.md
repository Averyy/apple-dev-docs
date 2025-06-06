# highlightColor(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Returns the color the receiver uses when drawing the selection highlight.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlightColor(withFrame cellFrame: NSRect, in controlView: NSView) -> NSColor?
```

#### Return Value

The color the receiver uses when drawing the selection highlight.

#### Discussion

You should not assume that a cell would necessarily want to draw itself with the value returned from [`selectedControlColor`](nscolor/selectedcontrolcolor.md). A cell may wish to draw with different a selection highlight color depending on such things as the key state of its `controlView`.

## Parameters

- `cellFrame`: The bounding rectangle of the receiver.
- `controlView`: The control that manages the cell.

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func drawInterior(withFrame: NSRect, in: NSView)](nscell/drawinterior(withframe:in:).md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [var controlView: NSView?](nscell/controlview.md)
  The view associated with the cell.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](nscell/highlight(_:withframe:in:).md)
  Redraws the receiver with the specified highlight setting.
- [var isHighlighted: Bool](nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/highlightcolor(withframe:in:))*