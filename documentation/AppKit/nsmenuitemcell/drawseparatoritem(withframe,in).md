# drawSeparatorItem(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws a menu item separator.

**Availability**:
- macOS

## Declaration

```swift
func drawSeparatorItem(withFrame cellFrame: NSRect, in controlView: NSView)
```

```objc
- (void) drawSeparatorItemWithFrame:(NSRect) cellFrame inView:(NSView *) controlView;
```

#### Discussion

This method uses the `cellFrame` parameter to calculate the rectangle in which to draw the menu item separator. This method uses the `controlView` to determine whether the separator item should be drawn normally or flipped.

You should not need to invoke this method directly. Subclasses may override this method to control the drawing of the separator.

## Parameters

- `cellFrame`: A rectangle defining the receiver’s frame area.
- `controlView`: The view object that contains this cell (usually an [`NSControl`](../nscontrol.md) object).

## See Also

### Related Documentation
- [var isFlipped: Bool](../nsview/isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
### Drawing the Menu Item
- [func drawBorderAndBackground(withFrame: NSRect, in: NSView)](./drawborderandbackground%28withframe,in%29.md)
  Draws the borders and background associated with the receiver’s menu item (if any).
- [func drawImage(withFrame: NSRect, in: NSView)](./drawimage%28withframe,in%29.md)
  Draws the image associated with the menu item.
- [func drawKeyEquivalent(withFrame: NSRect, in: NSView)](./drawkeyequivalent%28withframe,in%29.md)
  Draws the key equivalent associated with the menu item.
- [func drawStateImage(withFrame: NSRect, in: NSView)](./drawstateimage%28withframe,in%29.md)
  Draws the state image associated with the menu item.
- [func drawTitle(withFrame: NSRect, in: NSView)](./drawtitle%28withframe,in%29.md)
  Draws the title associated with the menu item.
- [var needsDisplay: Bool](./needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/drawseparatoritem(withframe:in:))*