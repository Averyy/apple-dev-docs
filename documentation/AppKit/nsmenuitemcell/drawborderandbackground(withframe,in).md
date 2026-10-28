# drawBorderAndBackground(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the borders and background associated with the receiver’s menu item (if any).

**Availability**:
- macOS

## Declaration

```swift
func drawBorderAndBackground(withFrame cellFrame: NSRect, in controlView: NSView)
```

```objc
- (void) drawBorderAndBackgroundWithFrame:(NSRect) cellFrame inView:(NSView *) controlView;
```

## Discussion

This method invokes the `NSCell` method [`imageRect(forBounds:)`](../nscell/imagerect%28forbounds%29.md), passing it `cellFrame`, to calculate the rectangle in which to draw the image. The cell invokes this method before invoking the methods to draw the other menu item components.

## Parameters

- `cellFrame`: A rectangle defining the receiver’s frame area.
- `controlView`: The view object that contains this cell (usually an [`NSControl`](../nscontrol.md) object).

## See Also

### Related Documentation
- [func draw(withFrame: NSRect, in: NSView)](../nscell/draw%28withframe,in%29.md)
  Draws the receiver’s border and then draws the interior of the cell.
### Drawing the Menu Item
- [func drawImage(withFrame: NSRect, in: NSView)](./drawimage%28withframe,in%29.md)
  Draws the image associated with the menu item.
- [func drawKeyEquivalent(withFrame: NSRect, in: NSView)](./drawkeyequivalent%28withframe,in%29.md)
  Draws the key equivalent associated with the menu item.
- [func drawSeparatorItem(withFrame: NSRect, in: NSView)](./drawseparatoritem%28withframe,in%29.md)
  Draws a menu item separator.
- [func drawStateImage(withFrame: NSRect, in: NSView)](./drawstateimage%28withframe,in%29.md)
  Draws the state image associated with the menu item.
- [func drawTitle(withFrame: NSRect, in: NSView)](./drawtitle%28withframe,in%29.md)
  Draws the title associated with the menu item.
- [var needsDisplay: Bool](./needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/drawborderandbackground(withframe:in:))*