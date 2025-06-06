# controlView

**Framework**: AppKit  
**Kind**: property

The view associated with the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var controlView: NSView? { get set }
```

#### Discussion

This property contains the view associated with the cell. This view is normally an [`NSControl`](nscontrol.md) object. The default value of this property is `nil`.

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](nscell/highlightcolor(withframe:in:).md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](nscell/drawinterior(withframe:in:).md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](nscell/highlight(_:withframe:in:).md)
  Redraws the receiver with the specified highlight setting.
- [var isHighlighted: Bool](nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/controlview)*