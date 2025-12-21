# hyphenationFactor

**Framework**: UIKit  
**Kind**: property

The paragraph’s threshold for hyphenation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hyphenationFactor: Float { get set }
```

#### Discussion

Valid values lie between `0.0` and `1.0` inclusive. The default value is `0.0`. Hyphenation is attempted when the ratio of the text width (as broken without hyphenation) to the width of the line fragment is less than the hyphenation factor. When the paragraph’s hyphenation factor is `0.0`, the layout manager’s hyphenation factor is used instead. When both are `0.0`, hyphenation is disabled. This property detects the user-selected language by examining the first item in `preferredLanguages`.

## See Also

- [let kCTLanguageAttributeName: CFString](../CoreText/kCTLanguageAttributeName.md)
  The name of the text language.
- [var lineBreakMode: NSLineBreakMode](nsmutableparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var usesDefaultHyphenation: Bool](nsmutableparagraphstyle/usesdefaulthyphenation.md)
- [var tighteningFactorForTruncation: Float](../AppKit/NSMutableParagraphStyle/tighteningFactorForTruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/hyphenationfactor)*