# needsDisplay

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the menu item needs to be displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var needsDisplay: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) when you want the menu item to be drawn.

## See Also

- [func drawBorderAndBackground(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawborderandbackground(withframe:in:).md)
  Draws the borders and background associated with the receiver’s menu item (if any).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/needsdisplay)*