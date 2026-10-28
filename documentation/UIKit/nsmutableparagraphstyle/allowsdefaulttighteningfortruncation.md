# allowsDefaultTighteningForTruncation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allowsDefaultTighteningForTruncation: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsDefaultTighteningForTruncation;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), the system tries to reduce the space between characters before truncating characters. The system performs this tightening in cases where the text would not otherwise fit in the available space. The maximum amount of tightening performed by the system is dependent on the font, line width, and other factors.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Setting line-break information
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](./usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float](../../AppKit/nsmutableparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/allowsdefaulttighteningfortruncation)*