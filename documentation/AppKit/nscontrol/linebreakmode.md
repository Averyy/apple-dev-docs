# lineBreakMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The line break mode to use for text in the control’s cell.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

```objc
@property NSLineBreakMode lineBreakMode;
```

## Discussion

For a list of possible values, see [`NSLineBreakMode`](../nslinebreakmode.md).

## See Also

### Formatting Text
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment mode of the text in the receiver’s cell.
- [var font: NSFont?](./font.md)
  The font used to draw text in the receiver’s cell.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](./formatter.md)
  The receiver’s formatter.
- [var baseWritingDirection: NSWritingDirection](./basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/linebreakmode)*