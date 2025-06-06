# alignment

**Framework**: AppKit  
**Kind**: property

The alignment mode of the text in the receiver’s cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var alignment: NSTextAlignment { get set }
```

#### Discussion

The value of this property can be one of the following constants: `NSLeftTextAlignment`, `NSRightTextAlignment`,`NSCenterTextAlignment`, `NSJustifiedTextAlignment`, or `NSNaturalTextAlignment`. The default value is `NSNaturalTextAlignment`. Setting this property while the cell is currently being edited aborts the edits to change the alignment.

## See Also

- [var font: NSFont?](nscontrol/font.md)
  The font used to draw text in the receiver’s cell.
- [var lineBreakMode: NSLineBreakMode](nscontrol/linebreakmode.md)
  The line break mode to use for text in the control’s cell.
- [var usesSingleLineMode: Bool](nscontrol/usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](nscontrol/formatter.md)
  The receiver’s formatter.
- [var baseWritingDirection: NSWritingDirection](nscontrol/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/alignment)*