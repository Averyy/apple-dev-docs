# font

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font used to draw text in the receiver’s cell.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var font: NSFont? { get set }
```

```objc
@property (copy, nullable) NSFont * font;
```

#### Discussion

If the cell is being edited, setting this property causes the text in the cell to be redrawn in the new font, and the cell’s editor (the `NSText` object used globally for editing) is updated with the new font object.

## See Also

### Formatting Text
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment mode of the text in the receiver’s cell.
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The line break mode to use for text in the control’s cell.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](./formatter.md)
  The receiver’s formatter.
- [var baseWritingDirection: NSWritingDirection](./basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/font)*