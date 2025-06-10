# UIBaselineAdjustment

**Framework**: UIKit  
**Kind**: enum

Vertical adjustment options.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum UIBaselineAdjustment
```

#### Overview

Baseline adjustment options determine how to adjust the position of text in cases where the text must be drawn using a different font size than the one originally specified. For example, with the [`UIBaselineAdjustment.alignBaselines`](uibaselineadjustment/alignbaselines.md) option, the position of the baseline remains fixed at its initial location while the text appears to move toward that baseline. Similarly, the [`UIBaselineAdjustment.none`](uibaselineadjustment/none.md) option makes it appear as if the text is moving upwards toward the top-left corner of the bounding box.

## Topics

### Constants
- [UIBaselineAdjustment.alignBaselines](uibaselineadjustment/alignbaselines.md)
  Adjust text relative to the position of its baseline.
- [UIBaselineAdjustment.alignCenters](uibaselineadjustment/aligncenters.md)
  Adjust text relative to the center of its bounding box.
- [UIBaselineAdjustment.none](uibaselineadjustment/none.md)
  Adjust text relative to the top-left corner of the bounding box.
### Initializers
- [init?(rawValue: Int)](uibaselineadjustment/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSStringDrawingContext](nsstringdrawingcontext.md)
  An object that manages metrics for drawing attributed strings.
- [struct NSStringDrawingOptions](nsstringdrawingoptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaselineadjustment)*