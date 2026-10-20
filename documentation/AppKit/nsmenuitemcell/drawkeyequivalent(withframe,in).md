# drawKeyEquivalent(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the key equivalent associated with the menu item.

**Availability**:
- macOS

## Declaration

```swift
func drawKeyEquivalent(withFrame cellFrame: NSRect, in controlView: NSView)
```

```objc
- (void) drawKeyEquivalentWithFrame:(NSRect) cellFrame inView:(NSView *) controlView;
```

#### Discussion

This method invokes [`keyEquivalentRect(forBounds:)`](./keyequivalentrect%28forbounds%29.md), passing it `cellFrame`, to calculate the rectangle in which to draw the key equivalent. This method is invoked by the cell’s `drawWithFrame:` method. You should not need to invoke it directly. Subclasses may override this method to control the drawing of the key equivalent.

## Parameters

- `cellFrame`: A rectangle defining the receiver’s frame area.
- `controlView`: The view object that contains this cell (usually an [`NSControl`](../nscontrol.md) object).

## See Also

### Drawing the Menu Item
- [func drawBorderAndBackground(withFrame: NSRect, in: NSView)](./drawborderandbackground%28withframe,in%29.md)
  Draws the borders and background associated with the receiver’s menu item (if any).
- [func drawImage(withFrame: NSRect, in: NSView)](./drawimage%28withframe,in%29.md)
  Draws the image associated with the menu item.
- [func drawSeparatorItem(withFrame: NSRect, in: NSView)](./drawseparatoritem%28withframe,in%29.md)
  Draws a menu item separator.
- [func drawStateImage(withFrame: NSRect, in: NSView)](./drawstateimage%28withframe,in%29.md)
  Draws the state image associated with the menu item.
- [func drawTitle(withFrame: NSRect, in: NSView)](./drawtitle%28withframe,in%29.md)
  Draws the title associated with the menu item.
- [var needsDisplay: Bool](./needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/drawkeyequivalent(withframe:in:))*