# textColor

**Framework**: AppKit  
**Kind**: property

The color of the text field’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var textColor: NSColor? { get set }
```

#### Discussion

> **Note**:  When the text field has an attributed string value, the system ignores the [`textColor`](nstextfield/textcolor.md), [`font`](nscontrol/font.md), [`alignment`](nscontrol/alignment.md), [`lineBreakMode`](nscontrol/linebreakmode.md), and `lineBreakStrategy` properties. Set the [`foregroundColor`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1533563-foregroundcolor), [`font`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528839-font), [`alignment`](nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

 When the text field has an attributed string value, the system ignores the [`textColor`](nstextfield/textcolor.md), [`font`](nscontrol/font.md), [`alignment`](nscontrol/alignment.md), [`lineBreakMode`](nscontrol/linebreakmode.md), and `lineBreakStrategy` properties. Set the [`foregroundColor`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1533563-foregroundcolor), [`font`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528839-font), [`alignment`](nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## See Also

- [var backgroundColor: NSColor?](nstextfield/backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var textColor: NSColor?](nstextfieldcell/textcolor.md)
  The color to use to draw the cell’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textcolor)*