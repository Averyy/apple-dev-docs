# NSLineBreakMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify what happens when a line is too long for a container.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum NSLineBreakMode
```

```c
enum NSLineBreakMode : NSInteger;
```

## Topics

### Constants
- [NSLineBreakMode.byWordWrapping](./nslinebreakmode/bywordwrapping.md)
  The value that indicates wrapping occurs at word boundaries, unless the word doesn’t fit on a single line.
- [NSLineBreakMode.byCharWrapping](./nslinebreakmode/bycharwrapping.md)
  The value that indicates wrapping occurs before the first character that doesn’t fit.
- [NSLineBreakMode.byClipping](./nslinebreakmode/byclipping.md)
  The value that indicates lines don’t extend past the edge of the text container.
- [NSLineBreakMode.byTruncatingHead](./nslinebreakmode/bytruncatinghead.md)
  The value that indicates that a line displays so that the end fits in the container and an ellipsis glyph indicates the missing text at the beginning of the line.
- [NSLineBreakMode.byTruncatingTail](./nslinebreakmode/bytruncatingtail.md)
  The value that indicates a line displays so that the beginning fits in the container and an ellipsis glyph indicates the missing text at the end of the line.
- [NSLineBreakMode.byTruncatingMiddle](./nslinebreakmode/bytruncatingmiddle.md)
  The value that indicates that a line displays so that the beginning and end fit in the container and an ellipsis glyph indicates the missing text in the middle.
### Initializers
- [init?(rawValue: Int)](./nslinebreakmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting line-break information
- [var lineBreakMode: NSLineBreakMode](./nsparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph that don’t fit within a container.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./nsparagraphstyle/linebreakstrategy-swift.property.md)
  The strategy for breaking lines while laying out paragraphs.
- [NSParagraphStyle.LineBreakStrategy](./nsparagraphstyle/linebreakstrategy-swift.struct.md)
  Constants that specify how the text system breaks lines while laying out paragraphs.
- [var hyphenationFactor: Float](./nsparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](./nsparagraphstyle/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float](../AppKit/nsparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](./nsparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslinebreakmode)*