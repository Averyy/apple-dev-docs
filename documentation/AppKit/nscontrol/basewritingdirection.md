# baseWritingDirection

**Framework**: AppKit  
**Kind**: property

The initial writing direction used to determine the actual writing direction for text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var baseWritingDirection: NSWritingDirection { get set }
```

#### Discussion

This property can have one of the following values: `NSWritingDirectionNatural`, `NSWritingDirectionLeftToRight`, or `NSWritingDirectionRightToLeft`. The default value is `NSWritingDirectionNatural`. The text system uses this value as a hint for calculating the actual direction for displaying Unicode characters. You should not need to access this value directly. If you know the base writing direction of the text you are rendering, you can set this property to specify that direction to the text system.

## See Also

- [var alignment: NSTextAlignment](nscontrol/alignment.md)
  The alignment mode of the text in the receiver’s cell.
- [var font: NSFont?](nscontrol/font.md)
  The font used to draw text in the receiver’s cell.
- [var lineBreakMode: NSLineBreakMode](nscontrol/linebreakmode.md)
  The line break mode to use for text in the control’s cell.
- [var usesSingleLineMode: Bool](nscontrol/usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](nscontrol/formatter.md)
  The receiver’s formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/basewritingdirection)*