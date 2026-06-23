# ScaleOption

**Framework**: Evaluations  
**Kind**: struct

A single option in a scoring scale.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ScaleOption
```

#### Overview

```swift
let option = ScaleOption(
    label: "Excellent",
    guideDescription: "The response is of exceptional quality.",
    value: 5.0
)
```

Each option defines a label, guide description, and numeric value. Options are presented to the model as judge in the scoring guide section of the prompt.

## Topics

### Initializers
- [init(label: String, guideDescription: String, value: Double)](scaleoption/init(label:guidedescription:value:).md)
  Creates a scale option.
### Instance Properties
- [let guideDescription: String](scaleoption/guidedescription.md)
  Rubric guidance shown to the judge for this option.
- [let label: String](scaleoption/label.md)
  A short label for this option (e.g., “excellent”, “pass”, “5”).
- [let value: Double](scaleoption/value.md)
  The numeric value for this option, used for metric aggregation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let options: [ScaleOption]](scoringscale/options.md)
  The scale options, ordered from highest to lowest value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scaleoption)*