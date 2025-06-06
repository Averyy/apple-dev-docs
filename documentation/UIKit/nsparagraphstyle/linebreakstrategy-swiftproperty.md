# lineBreakStrategy

**Framework**: UIKit  
**Kind**: property

The strategy for breaking lines while laying out paragraphs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get }
```

#### Discussion

Line-break strategies are collections of options the system uses to determine where to break lines in a paragraph. This is different from [`lineBreakMode`](nsparagraphstyle/linebreakmode.md), which controls how to lay out lines of text that don’t fit in a container. The system ignores this property if the paragraph style’s [`lineBreakMode`](nsparagraphstyle/linebreakmode.md) property specifies a mode that doesn’t support multiple lines, such as [`NSLineBreakMode.byClipping`](nslinebreakmode/byclipping.md).

The default value is [`NSLineBreakStrategyNone`](nslinebreakstrategy/nslinebreakstrategynone.md).

## See Also

- [var lineBreakMode: NSLineBreakMode](nsparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph that don’t fit within a container.
- [enum NSLineBreakMode](nslinebreakmode.md)
  Constants that specify what happens when a line is too long for a container.
- [NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct.md)
  Constants that specify how the text system breaks lines while laying out paragraphs.
- [var hyphenationFactor: Float](nsparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsparagraphstyle/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float { get }](../AppKit/NSParagraphStyle/tighteningFactorForTruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.property)*