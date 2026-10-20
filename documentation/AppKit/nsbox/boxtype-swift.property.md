# boxType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s box type.

**Availability**:
- macOS

## Declaration

```swift
var boxType: NSBox.BoxType { get set }
```

```objc
@property NSBoxType boxType;
```

#### Discussion

A constant describing the type of box. These constants are described in [`NSBox.BoxType`](./boxtype-swift.enum.md). By default, the box type of an `NSBox` is `NSBoxPrimary`.

## See Also

### Configuring Boxes
- [var borderRect: NSRect](./borderrect.md)
  The rectangle in which the receiver’s border is drawn.
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
- [var borderType: NSBorderType](./bordertype.md)
  The receiver’s border type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/boxtype-swift.property)*