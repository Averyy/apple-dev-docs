# drawInterior(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawInterior(withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

Text-type `NSCell` objects display their contents in a rectangle slightly inset from `cellFrame` using a global `NSText` object. Image-type `NSCell` objects display their contents centered within `cellFrame`. If the proper attributes are set, this method also displays the dotted-line rectangle to indicate if the control is the first responder and highlights the cell. This method is invoked from the [`drawCellInside(_:)`](nscontrol/drawcellinside(_:).md) method of `NSControl` to visually update what the cell displays when its contents change. The drawing done by the `NSCell` implementation is minimal and becomes more complex in objects such as `NSButtonCell` and `NSSliderCell`.

This method draws the cell in the currently focused view, which can be different from the `controlView` passed in. Taking advantage of this is not recommended.

Subclasses often override this method to provide more sophisticated drawing of cell contents. Because [`draw(withFrame:in:)`](nscell/draw(withframe:in:).md) invokes [`drawInterior(withFrame:in:)`](nscell/drawinterior(withframe:in:).md) after it draws the cell’s border, do not invoke [`draw(withFrame:in:)`](nscell/draw(withframe:in:).md) in your override implementation.

## Parameters

- `cellFrame`: The bounding rectangle of the receiver, or a portion of the bounding rectangle.
- `controlView`: The control that manages the cell.

## See Also

- [var showsFirstResponder: Bool](nscell/showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](nscell/highlightcolor(withframe:in:).md)
  Returns the color the receiver uses when drawing the selection highlight.
- [var controlView: NSView?](nscell/controlview.md)
  The view associated with the cell.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](nscell/highlight(_:withframe:in:).md)
  Redraws the receiver with the specified highlight setting.
- [var isHighlighted: Bool](nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/drawinterior(withframe:in:))*