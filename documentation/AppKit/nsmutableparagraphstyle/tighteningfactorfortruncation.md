# tighteningFactorForTruncation

**Framework**: AppKit  
**Kind**: property

The threshold for using tightening as an alternative to truncation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var tighteningFactorForTruncation: Float { get set }
```

#### Discussion

When the line break mode specifies truncation, the text system attempts to tighten inter character spacing as an alternative to truncation, provided that the ratio of the text width to the line fragment width does not exceed 1.0 + the value of [`tighteningFactorForTruncation`](nsparagraphstyle/tighteningfactorfortruncation.md). Otherwise the text is truncated at a location determined by the line break mode. The default value is 0.05. This value can be a positive or negative value. Values less than or equal to 0.0 result in not tightening.

## See Also

- [var lineBreakMode: NSLineBreakMode](nsmutableparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](nsmutableparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsmutableparagraphstyle/usesdefaulthyphenation.md)
- [var allowsDefaultTighteningForTruncation: Bool](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/tighteningfactorfortruncation)*