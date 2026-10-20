# NSStringDrawingOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the rendering options for drawing a string.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSStringDrawingOptions
```

```c
enum NSStringDrawingOptions : NSInteger;
```

## Topics

### Constants
- [static var usesLineFragmentOrigin: NSStringDrawingOptions](./nsstringdrawingoptions/useslinefragmentorigin.md)
  Uses the line fragment origin instead of the baseline origin.
- [static var usesFontLeading: NSStringDrawingOptions](./nsstringdrawingoptions/usesfontleading.md)
  Uses the font leading for calculating line heights.
- [static var usesDeviceMetrics: NSStringDrawingOptions](./nsstringdrawingoptions/usesdevicemetrics.md)
  Uses image glyph bounds instead of typographic bounds.
- [static var truncatesLastVisibleLine: NSStringDrawingOptions](./nsstringdrawingoptions/truncateslastvisibleline.md)
  Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.
### Initializer
- [init(rawValue: Int)](./nsstringdrawingoptions/init%28rawvalue%29.md)
  Creates a structure that specifies the rendering options for drawing a string.
### Type Properties
- [static var optionsResolvesNaturalAlignmentWithBaseWritingDirection: NSStringDrawingOptions](./nsstringdrawingoptions/optionsresolvesnaturalalignmentwithbasewritingdirection.md)
  Specifies the behavior for resolving [`NSTextAlignment.natural`](./nstextalignment/natural.md) to the visual alignment.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Strings
- [class NSStringDrawingContext](./nsstringdrawingcontext.md)
  An object that manages metrics for drawing attributed strings.
- [enum UIBaselineAdjustment](./uibaselineadjustment.md)
  Vertical adjustment options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions)*