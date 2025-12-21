# lineBreakStrategy

**Framework**: UIKit  
**Kind**: property

The strategies that the text system may use to break lines while laying out the paragraph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

#### Discussion

Line-break strategies are collections of options the system uses to determine where to break lines in a paragraph. This is different from [`lineBreakMode`](nsparagraphstyle/linebreakmode.md), which controls how to lay out lines of text that don’t fit in a container. The system ignores this property if the paragraph style’s [`lineBreakMode`](nsparagraphstyle/linebreakmode.md) property specifies a mode that doesn’t support multiple lines, such as [`NSLineBreakMode.byClipping`](nslinebreakmode/byclipping.md).

The default value is [`NSLineBreakStrategyNone`](nslinebreakstrategy/nslinebreakstrategynone.md).

## See Also

- [var lineBreakMode: NSLineBreakMode](nsmutableparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var hyphenationFactor: Float](nsmutableparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsmutableparagraphstyle/usesdefaulthyphenation.md)
- [var tighteningFactorForTruncation: Float](../AppKit/NSMutableParagraphStyle/tighteningFactorForTruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/linebreakstrategy)*