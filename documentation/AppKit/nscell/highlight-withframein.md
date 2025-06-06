# highlight(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Redraws the receiver with the specified highlight setting.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlight(_ flag: Bool, withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

Note that the `NSCell` highlighting does not appear when highlighted cells are printed (although instances of `NSTextFieldCell`, `NSButtonCell`, and others can print themselves highlighted). Generally, you cannot depend on highlighting being printed because implementations of this method may choose (or not choose) to use transparency.

## Parameters

- `flag`: If  , the cell is redrawn with a highlight; otherwise, if  , the highlight is removed.
- `cellFrame`: The bounding rectangle of the receiver.
- `controlView`: The control that manages the cell.

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](nscell/highlightcolor(withframe:in:).md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](nscell/drawinterior(withframe:in:).md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [var controlView: NSView?](nscell/controlview.md)
  The view associated with the cell.
- [var isHighlighted: Bool](nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/highlight(_:withframe:in:))*