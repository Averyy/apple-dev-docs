# allowsDefaultTighteningForTruncation

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the system tightens character spacing before truncating text.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var allowsDefaultTighteningForTruncation: Bool { get }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/swift/true), the system tries to reduce the space between characters before truncating characters. The system performs this tightening in cases where the text wouldn’t otherwise fit in the available space. The maximum amount of tightening performed by the system is dependent on the font, line width, and other factors.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var lineBreakMode: NSLineBreakMode](nsparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph that don’t fit within a container.
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
- [var tighteningFactorForTruncation: Float](nsparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/allowsdefaulttighteningfortruncation)*