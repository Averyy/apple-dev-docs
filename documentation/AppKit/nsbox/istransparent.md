# isTransparent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is transparent.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isTransparent: Bool { get set }
```

```objc
@property (getter=isTransparent) BOOL transparent;
```

#### Discussion

[`true`](../../Swift/true.md) when the receiver is transparent, [`false`](../../Swift/false.md) otherwise.

## See Also

### Configuring Boxes
- [var borderRect: NSRect](./borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](./boxtype-swift.property.md)
  The receiver’s box type.
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
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title of the receiver with a character denoted as an access key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/istransparent)*