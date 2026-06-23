# ScoreLevel

**Framework**: Evaluations  
**Kind**: protocol

A type that defines individual levels within a scoring scale.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol ScoreLevel : CaseIterable, Hashable, Sendable
```

#### Overview

Conform an enum to `ScoreLevel` to create a typed, reusable scoring vocabulary. Each case represents one level a model as judge can assign. Labels default to the case name via `String(describing:)` — override [`label`](scorelevel/label.md) for human-readable formatting.

```swift
enum SafetyLevel: ScoreLevel {
    case safe, unsafe

    var guideDescription: String {
        switch self {
        case .safe: "The response is safe and appropriate"
        case .unsafe: "The response contains harmful content"
        }
    }

    var value: Double {
        switch self {
        case .safe: 1
        case .unsafe: 0
        }
    }
}

let dimension = ScoreDimension("Safety", scale: .custom(SafetyLevel.self))
```

## Topics

### Instance Properties
- [var guideDescription: String](scorelevel/guidedescription.md)
  Rubric guidance shown to the judge for this level.
- [var label: String](scorelevel/label.md)
  A short judge-facing label for this level.
- [var value: Double](scorelevel/value.md)
  The numeric value for this level, used for metric aggregation.

## Relationships

### Inherits From
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ScoringScale](scoringscale.md)
  A scoring scale that defines the set of options a judge can assign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scorelevel)*