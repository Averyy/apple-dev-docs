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
var hyphenationFactor: Float { get }
```

#### Discussion

The system attempts hyphenation when the ratio of the text width (as broken without hyphenation) to the width of the line fragment is less than the hyphenation factor. When the paragraph’s hyphenation factor is `0.0`, the system uses the layout manager’s hyphenation factor instead. The system disables hyphenation when both are `0.0`. This property detects the user-selected language by examining the first item in [`preferredLanguages`](https://developer.apple.com/documentation/foundation/nslocale/1415614-preferredlanguages).

## See Also

- [let kCTLanguageAttributeName: CFString](../CoreText/kCTLanguageAttributeName.md)
  The name of the text language.
- [var lineBreakMode: NSLineBreakMode](nsparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph that don’t fit within a container.
- [enum NSLineBreakMode](nslinebreakmode.md)
  Constants that specify what happens when a line is too long for a container.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.property.md)
  The strategy for breaking lines while laying out paragraphs.
- [NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct.md)
  Constants that specify how the text system breaks lines while laying out paragraphs.
- [var usesDefaultHyphenation: Bool](nsparagraphstyle/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float { get }](../AppKit/NSParagraphStyle/tighteningFactorForTruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/hyphenationfactor)*