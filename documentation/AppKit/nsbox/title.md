# title

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s title.

**Availability**:
- macOS

## Declaration

```swift
var title: String { get set }
```

```objc
@property (copy) NSString * title;
```

## Discussion

The title of the `NSBox`. By default, a box’s title is “Title.” If the size of the new title is different from that of the old title, the content view is resized to absorb the difference.

## See Also

### Configuring Boxes
- [var borderRect: NSRect](./borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](./boxtype-swift.property.md)
  The receiver’s box type.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
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
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title of the receiver with a character denoted as an access key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/title)*