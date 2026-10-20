# controlView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view associated with the cell.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var controlView: NSView? { get set }
```

```objc
@property (assign, nullable) NSView * controlView;
```

#### Discussion

This property contains the view associated with the cell. This view is normally an [`NSControl`](../nscontrol.md) object. The default value of this property is `nil`.

## See Also

### Drawing and Highlighting
- [func draw(withFrame: NSRect, in: NSView)](./draw%28withframe,in%29.md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](./highlightcolor%28withframe,in%29.md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](./drawinterior%28withframe,in%29.md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](./highlight%28_,withframe,in%29.md)
  Redraws the receiver with the specified highlight setting.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/controlview)*