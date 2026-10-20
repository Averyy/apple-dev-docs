# titlePosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A constant representing the title position.

**Availability**:
- macOS

## Declaration

```swift
var titlePosition: NSBox.TitlePosition { get set }
```

```objc
@property NSTitlePosition titlePosition;
```

#### Discussion

A constant representing the position of the receiver’s title. See [`NSBox.TitlePosition`](./titleposition-swift.enum.md) for a list of these constants. If the new title position changes the size of the box’s border area, the content view is resized to absorb the difference, and the box is marked as needing redisplay.

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
- [var titleCell: Any](./titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](./titlerect.md)
  The rectangle in which the receiver’s title is drawn.
- [var borderType: NSBorderType](./bordertype.md)
  The receiver’s border type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/titleposition-swift.property)*