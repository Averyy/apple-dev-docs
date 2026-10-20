# borderType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s border type.

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

> **Deprecated**: borderType is only applicable to NSBoxOldStyle, which is deprecated. To replace a borderType of NSNoBorder, use the `transparent` property.

## Declaration

```swift
var borderType: NSBorderType { get set }
```

```objc
@property NSBorderType borderType;
```

#### Discussion

A constant describing the type of border. Border types are defined in `NSView.h`. Currently, the following border types are defined: `NSNoBorder`,`NSLineBorder`,`NSBezelBorder`, `NSGrooveBorder`.

By default, the border type of an `NSBox` is `NSGrooveBorder`.

If the size of the new border is different from that of the old border, the content view is resized to absorb the difference, and the box is marked for redisplay.

## See Also

### Configuring Boxes
- [var borderRect: NSRect](./borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](./boxtype-swift.property.md)
  The receiver’s box type.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
- [var title: String](./title.md)
  The receiver’s title.
- [var titleFont: NSFont](./titlefont.md)
  The font object used to draw the receiver’s title.
- [var titlePosition: NSBox.TitlePosition](./titleposition-swift.property.md)
  A constant representing the title position.
- [var titleCell: Any](./titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](./titlerect.md)
  The rectangle in which the receiver’s title is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/bordertype)*