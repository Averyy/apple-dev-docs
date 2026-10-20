# needsDisplay

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the menu item needs to be displayed.

**Availability**:
- macOS

## Declaration

```swift
var needsDisplay: Bool { get set }
```

```objc
@property BOOL needsDisplay;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) when you want the menu item to be drawn.

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
- [func drawTitle(withFrame: NSRect, in: NSView)](./drawtitle%28withframe,in%29.md)
  Draws the title associated with the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/needsdisplay)*