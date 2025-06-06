# font

**Framework**: AppKit  
**Kind**: property

The font used to draw text in the receiver’s cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var font: NSFont? { get set }
```

#### Discussion

If the cell is being edited, setting this property causes the text in the cell to be redrawn in the new font, and the cell’s editor (the `NSText` object used globally for editing) is updated with the new font object.

## See Also

- [var alignment: NSTextAlignment](nscontrol/alignment.md)
  The alignment mode of the text in the receiver’s cell.
- [var lineBreakMode: NSLineBreakMode](nscontrol/linebreakmode.md)
  The line break mode to use for text in the control’s cell.
- [var usesSingleLineMode: Bool](nscontrol/usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](nscontrol/formatter.md)
  The receiver’s formatter.
- [var baseWritingDirection: NSWritingDirection](nscontrol/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/font)*