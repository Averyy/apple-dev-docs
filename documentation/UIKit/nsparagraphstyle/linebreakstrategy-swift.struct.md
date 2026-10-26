# NSParagraphStyle.LineBreakStrategy

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify how the text system breaks lines while laying out paragraphs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct LineBreakStrategy
```

```c
enum NSLineBreakStrategy : NSUInteger;
```

#### Overview

Line break strategy describes a collection of options that can affect where line breaks are placed in a paragraph. This is independent from line break mode, which describes what happens when text is too long to fit within its container. These options won’t have any effect when used with line break modes that don’t support multiple lines, like clipping or truncating middle.

Constants that specify how the text system breaks lines while laying out paragraphs.

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
- [var tighteningFactorForTruncation: Float](../../AppKit/nsparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct)*