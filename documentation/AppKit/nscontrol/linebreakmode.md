# lineBreakMode

**Framework**: AppKit  
**Kind**: property

The line break mode to use for text in the control’s cell.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var lineBreakMode: NSLineBreakMode { get set }
```

#### Discussion

For a list of possible values, see [`NSLineBreakMode`](nslinebreakmode.md).

## See Also

- [var alignment: NSTextAlignment](nscontrol/alignment.md)
  The alignment mode of the text in the receiver’s cell.
- [var font: NSFont?](nscontrol/font.md)
  The font used to draw text in the receiver’s cell.
- [var usesSingleLineMode: Bool](nscontrol/usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](nscontrol/formatter.md)
  The receiver’s formatter.
- [var baseWritingDirection: NSWritingDirection](nscontrol/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/linebreakmode)*