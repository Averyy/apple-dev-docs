# lineBreakStrategy

**Framework**: Appkit  
**Kind**: property

The strategy that the system uses to break lines when laying out multiple lines of text.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

#### Discussion

The default value for editable text fields is [`NSLineBreakStrategyNone`](nslinebreakstrategy/nslinebreakstrategynone.md) to match the field editor’s behavior. The default value for selectable, uneditable text fields is [`standard`](nsparagraphstyle/linebreakstrategy-swift.struct/standard.md).

> **Note**:  When the text field has an attributed string value, the system ignores the [`textColor`](nstextfield/textcolor.md), [`font`](nscontrol/font.md), [`alignment`](nscontrol/alignment.md), [`lineBreakMode`](nscontrol/linebreakmode.md), and `lineBreakStrategy` properties. Set the [`foregroundColor`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1533563-foregroundcolor), [`font`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528839-font), [`alignment`](nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## See Also

- [var allowsDefaultTighteningForTruncation: Bool](nstextfield/allowsdefaulttighteningfortruncation.md)
  A Boolean value that controls whether single-line text fields tighten intercharacter spacing before truncating the text.
- [var maximumNumberOfLines: Int](nstextfield/maximumnumberoflines.md)
  The maximum number of lines a wrapping text field displays before clipping or truncating the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nstextfield/linebreakstrategy)*