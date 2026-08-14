# ScoringMode

**Framework**: Evaluations  
**Kind**: enum

The scoring constraint mode for a model-as-judge evaluator.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum ScoringMode
```

#### Overview

```swift
let mode: ScoringMode = .discrete
```

Controls whether the judge model can return any floating-point score (continuous) or is structurally constrained to return exactly one of the defined scale values (discrete).

## Topics

### Enumeration Cases
- [ScoringMode.continuous](scoringmode/continuous.md)
  A mode that allows the model to return any floating-point value. The scale serves as a guide but is not enforced at the generation level.
- [ScoringMode.discrete](scoringmode/discrete.md)
  A mode that requires the model to return exactly one of the values defined in the scoring dimension’s scale, enforced using structured generation.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let dimensions: [ScoreDimension]](modeljudgeevaluator/dimensions.md)
  The dimensions this evaluator scores.
- [let scoringMode: ScoringMode](modeljudgeevaluator/scoringmode.md)
  The scoring constraint mode. See [`ScoringMode`](scoringmode.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringmode)*