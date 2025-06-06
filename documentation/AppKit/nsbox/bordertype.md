# borderType

**Framework**: AppKit  
**Kind**: property

The receiver’s border type.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var borderType: NSBorderType { get set }
```

#### Discussion

A constant describing the type of border. Border types are defined in `NSView.h`. Currently, the following border types are defined: `NSNoBorder`,`NSLineBorder`,`NSBezelBorder`, `NSGrooveBorder`.

By default, the border type of an `NSBox` is `NSGrooveBorder`.

If the size of the new border is different from that of the old border, the content view is resized to absorb the difference, and the box is marked for redisplay.

## See Also

- [var borderRect: NSRect](nsbox/borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](nsbox/boxtype-swift.property.md)
  The receiver’s box type.
- [var isTransparent: Bool](nsbox/istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
- [var title: String](nsbox/title.md)
  The receiver’s title.
- [var titleFont: NSFont](nsbox/titlefont.md)
  The font object used to draw the receiver’s title.
- [var titlePosition: NSBox.TitlePosition](nsbox/titleposition-swift.property.md)
  A constant representing the title position.
- [var titleCell: Any](nsbox/titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](nsbox/titlerect.md)
  The rectangle in which the receiver’s title is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/bordertype)*