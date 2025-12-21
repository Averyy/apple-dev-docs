# allowsDefaultTighteningForTruncation

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var allowsDefaultTighteningForTruncation: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the system tries to reduce the space between characters before truncating characters. The system performs this tightening in cases where the text would not otherwise fit in the available space. The maximum amount of tightening performed by the system is dependent on the font, line width, and other factors.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var lineBreakMode: NSLineBreakMode](nsmutableparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](nsmutableparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsmutableparagraphstyle/usesdefaulthyphenation.md)
- [var tighteningFactorForTruncation: Float](nsmutableparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/allowsdefaulttighteningfortruncation)*