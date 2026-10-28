# lineBreakStrategy

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The strategy that the system uses to break lines when laying out multiple lines of text.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

```objc
@property NSLineBreakStrategy lineBreakStrategy;
```

## Discussion

The default value for editable text fields is [`NSLineBreakStrategyNone`](../nslinebreakstrategy/nslinebreakstrategynone.md) to match the field editor’s behavior. The default value for selectable, uneditable text fields is [`standard`](../nsparagraphstyle/linebreakstrategy-swift.struct/standard.md).

> **Note**:  When the text field has an attributed string value, the system ignores the [`textColor`](./textcolor.md), [`font`](../nscontrol/font.md), [`alignment`](../nscontrol/alignment.md), [`lineBreakMode`](../nscontrol/linebreakmode.md), and `lineBreakStrategy` properties. Set the [`foregroundColor`](../../Foundation/nsattributedstring/key/foregroundcolor.md), [`font`](../../Foundation/nsattributedstring/key/font.md), [`alignment`](../nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](../nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](../nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## See Also

### Configuring line wrapping
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that controls whether single-line text fields tighten intercharacter spacing before truncating the text.
- [var maximumNumberOfLines: Int](./maximumnumberoflines.md)
  The maximum number of lines a wrapping text field displays before clipping or truncating the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/linebreakstrategy)*