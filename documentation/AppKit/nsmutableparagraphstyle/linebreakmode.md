# lineBreakMode

**Framework**: AppKit  
**Kind**: property

The mode for breaking lines in the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

#### Discussion

This property controls how the text system lays out lines that don’t fit in its container, such as by truncating with an ellipsis (…) or clipping the text. This is different from [`NSParagraphStyle.LineBreakStrategy`](nsparagraphstyle/linebreakstrategy-swift.struct.md) , which controls where the system places line breaks in a paragraph.

## See Also

- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](nsmutableparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsmutableparagraphstyle/usesdefaulthyphenation.md)
- [var tighteningFactorForTruncation: Float](nsmutableparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/linebreakmode)*