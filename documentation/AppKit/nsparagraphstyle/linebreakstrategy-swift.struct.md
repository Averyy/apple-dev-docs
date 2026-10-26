# NSParagraphStyle.LineBreakStrategy

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify how the text system breaks lines while laying out paragraphs.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct LineBreakStrategy
```

```c
enum NSLineBreakStrategy : NSUInteger;
```

## Topics

### Getting the line-break styles
- [static var pushOut: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy-swift.struct/pushout.md)
  The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy-swift.struct/hangulwordpriority.md)
  The text system prohibits breaking between Hangul characters.
- [static var standard: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy-swift.struct/standard.md)
  The text system uses the same configuration of line-break strategies that it uses for standard UI labels.
- [NSLineBreakStrategyNone](../nslinebreakstrategy/nslinebreakstrategynone.md)
  The text system doesn’t use any line-break strategies.
### Creating a line-break style
- [init(rawValue: UInt)](./linebreakstrategy-swift.struct/init%28rawvalue%29.md)
  Creates a line-break strategy with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting line-break information
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The mode for breaking lines in the paragraph that don’t fit within a container.
- [enum NSLineBreakMode](../nslinebreakmode.md)
  Constants that specify what happens when a line is too long for a container.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy-swift.property.md)
  The strategy for breaking lines while laying out paragraphs.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](./usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float](./tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/linebreakstrategy-swift.struct)*