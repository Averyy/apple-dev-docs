# setTitleWithMnemonic:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the title of the receiver with a character denoted as an access key.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) setTitleWithMnemonic:(NSString *) stringWithAmpersand;
```

## Discussion

Mnemonics are not supported in macOS.

By default, a box’s title is “Title.” The content view is not automatically resized, and the box is not marked for redisplay.

## See Also

### Related Documentation
- [- setTitleWithMnemonic:](../nscell/settitlewithmnemonic_.md)
  Sets the title of the receiver with one character in the string denoted as an access key.
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
- [var borderType: NSBorderType](./bordertype.md)
  The receiver’s border type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/settitlewithmnemonic:)*