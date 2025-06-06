# drawBorderAndBackground(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the borders and background associated with the receiver’s menu item (if any).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawBorderAndBackground(withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

This method invokes the `NSCell` method [`imageRect(forBounds:)`](nscell/imagerect(forbounds:).md), passing it `cellFrame`, to calculate the rectangle in which to draw the image. The cell invokes this method before invoking the methods to draw the other menu item components.

## Parameters

- `cellFrame`: A rectangle defining the receiver’s frame area.
- `controlView`: The view object that contains this cell (usually an   object).

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func drawImage(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawimage(withframe:in:).md)
  Draws the image associated with the menu item.
- [func drawKeyEquivalent(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawkeyequivalent(withframe:in:).md)
  Draws the key equivalent associated with the menu item.
- [func drawSeparatorItem(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawseparatoritem(withframe:in:).md)
  Draws a menu item separator.
- [func drawStateImage(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawstateimage(withframe:in:).md)
  Draws the state image associated with the menu item.
- [func drawTitle(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawtitle(withframe:in:).md)
  Draws the title associated with the menu item.
- [var needsDisplay: Bool](nsmenuitemcell/needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/drawborderandbackground(withframe:in:))*