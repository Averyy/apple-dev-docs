# usesDefaultHyphenation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 12.0+

## Declaration

```swift
var usesDefaultHyphenation: Bool { get set }
```

```objc
@property (readwrite) BOOL usesDefaultHyphenation;
```

## See Also

### Setting line-break information
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var tighteningFactorForTruncation: Float](./tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/usesdefaulthyphenation)*