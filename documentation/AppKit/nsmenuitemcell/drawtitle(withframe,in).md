# drawTitle(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the title associated with the menu item.

**Availability**:
- macOS

## Declaration

```swift
func drawTitle(withFrame cellFrame: NSRect, in controlView: NSView)
```

```objc
- (void) drawTitleWithFrame:(NSRect) cellFrame inView:(NSView *) controlView;
```

## Discussion

This method invokes [`titleRect(forBounds:)`](./titlerect%28forbounds%29.md), passing it `cellFrame`, to calculate the rectangle in which to draw the title. The `controlView` parameter specifies the view that contains this cell.This method is invoked by the cell’s `drawWithFrame:` method. You should not need to invoke it directly. Subclasses may override this method to control the drawing of the title.

## Parameters

- `cellFrame`: A rectangle defining the receiver’s frame area.
- `controlView`: The view object that contains this cell (usually an [`NSControl`](../nscontrol.md) object).

## See Also

### Drawing the Menu Item
- [func drawBorderAndBackground(withFrame: NSRect, in: NSView)](./drawborderandbackground%28withframe,in%29.md)
  Draws the borders and background associated with the receiver’s menu item (if any).
- [func drawImage(withFrame: NSRect, in: NSView)](./drawimage%28withframe,in%29.md)
  Draws the image associated with the menu item.
- [func drawKeyEquivalent(withFrame: NSRect, in: NSView)](./drawkeyequivalent%28withframe,in%29.md)
  Draws the key equivalent associated with the menu item.
- [func drawSeparatorItem(withFrame: NSRect, in: NSView)](./drawseparatoritem%28withframe,in%29.md)
  Draws a menu item separator.
- [func drawStateImage(withFrame: NSRect, in: NSView)](./drawstateimage%28withframe,in%29.md)
  Draws the state image associated with the menu item.
- [var needsDisplay: Bool](./needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/drawtitle(withframe:in:))*