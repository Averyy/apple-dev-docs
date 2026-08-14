# usesDefaultHyphenation

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var usesDefaultHyphenation: Bool { get set }
```

#### Discussion

The system determines the exact hyphenation logic dynamically by examining the layout context such as language, platform, etc. When `true`, it affects the return value from [`hyphenationFactor`](nsmutableparagraphstyle/hyphenationfactor.md) when the property is set to `0.0`.

## See Also

- [var lineBreakMode: NSLineBreakMode](nsmutableparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](nsmutableparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var tighteningFactorForTruncation: Float](../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/usesdefaulthyphenation)*