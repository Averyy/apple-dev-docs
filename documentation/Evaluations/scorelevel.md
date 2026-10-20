# ScoreLevel

**Framework**: Evaluations  
**Kind**: protocol  
**Role**: Protocol

A type that defines individual levels within a scoring scale.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
protocol ScoreLevel : CaseIterable, Hashable, Sendable
```

#### Overview

Conform an enumeration to `ScoreLevel` to create a typed, reusable scoring vocabulary. Each case represents one level a model judge can assign. Labels default to the case name using `String(describing:)`. Override [`label`](./scorelevel/label.md) for human-readable formatting.

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
- [var guideDescription: String](./scorelevel/guidedescription.md)
  Rubric guidance the model judge references for this level.
- [var label: String](./scorelevel/label.md)
  A short judge-facing label for this level.
- [var value: Double](./scorelevel/value.md)
  The numeric value for this level that metric aggregation references.

## Relationships

### Inherits From
- [CaseIterable](../Swift/caseiterable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining scales
- [struct ScoringScale](./scoringscale.md)
  A scoring scale that defines the set of options a judge can assign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scorelevel)*