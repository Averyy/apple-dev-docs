# lineBreakMode

**Framework**: UIKit  
**Kind**: property

The mode for breaking lines in the paragraph that don’t fit within a container.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineBreakMode: NSLineBreakMode { get }
```

#### Discussion

This property controls how the text system lays out lines that don’t fit in its container, such as by truncating with an ellipsis (…) or clipping the text. This is different from [`NSParagraphStyle.LineBreakStrategy`](nsparagraphstyle/linebreakstrategy-swift.struct.md), which controls where the system places line breaks in a paragraph.

## See Also

- [enum NSLineBreakMode](nslinebreakmode.md)
  Constants that specify what happens when a line is too long for a container.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.property.md)
  The strategy for breaking lines while laying out paragraphs.
- [NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct.md)
  Constants that specify how the text system breaks lines while laying out paragraphs.
- [var hyphenationFactor: Float](nsparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsparagraphstyle/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float](../AppKit/NSParagraphStyle/tighteningFactorForTruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakmode)*