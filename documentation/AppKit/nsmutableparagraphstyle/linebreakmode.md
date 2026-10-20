# lineBreakMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The mode for breaking lines in the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

```objc
@property NSLineBreakMode lineBreakMode;
```

#### Discussion

This property controls how the text system lays out lines that don’t fit in its container, such as by truncating with an ellipsis (…) or clipping the text. This is different from [`NSParagraphStyle.LineBreakStrategy`](../nsparagraphstyle/linebreakstrategy-swift.struct.md) , which controls where the system places line breaks in a paragraph.

## See Also

### Setting line-break information
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](./usesdefaulthyphenation.md)
- [var tighteningFactorForTruncation: Float](./tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/linebreakmode)*