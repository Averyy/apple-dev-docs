# drawKeyEquivalent(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the key equivalent associated with the menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawKeyEquivalent(withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

This method invokes [`keyEquivalentRect(forBounds:)`](nsmenuitemcell/keyequivalentrect(forbounds:).md), passing it `cellFrame`, to calculate the rectangle in which to draw the key equivalent. This method is invoked by the cell’s `drawWithFrame:` method. You should not need to invoke it directly. Subclasses may override this method to control the drawing of the key equivalent.

## Parameters

- `cellFrame`: A rectangle defining the receiver’s frame area.
- `controlView`: The view object that contains this cell (usually an   object).

## See Also

- [func drawBorderAndBackground(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawborderandbackground(withframe:in:).md)
  Draws the borders and background associated with the receiver’s menu item (if any).
- [func drawImage(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawimage(withframe:in:).md)
  Draws the image associated with the menu item.
- [func drawSeparatorItem(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawseparatoritem(withframe:in:).md)
  Draws a menu item separator.
- [func drawStateImage(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawstateimage(withframe:in:).md)
  Draws the state image associated with the menu item.
- [func drawTitle(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawtitle(withframe:in:).md)
  Draws the title associated with the menu item.
- [var needsDisplay: Bool](nsmenuitemcell/needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/drawkeyequivalent(withframe:in:))*