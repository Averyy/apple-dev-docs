# ScoringScale

**Framework**: Evaluations  
**Kind**: struct

A scoring scale that defines the set of options a judge can assign.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ScoringScale
```

## Mentions

- [Designing effective model-as-judge evaluators](designing-effective-model-judges.md)

#### Overview

Use the factory methods to create scales from numeric dictionaries, pass/fail pairs, or typed [`ScoreLevel`](scorelevel.md) enums:

```swift
// Numeric scale
let _ = ScoringScale.numeric([5: "Flawless", 3: "Readable", 1: "Incomprehensible"])

// Pass/fail
let _ = ScoringScale.passFail(passDescription: "Safe", failDescription: "Unsafe")

// Typed enum
enum SafetyLevel: ScoreLevel {
    case safe, unsafe
    var guideDescription: String { self == .safe ? "Safe" : "Unsafe" }
    var value: Double { self == .safe ? 1 : 0 }
}
let _ = ScoringScale.custom(SafetyLevel.self)
```

## Topics

### Creating a scale
- [static func passFail(passDescription: String, failDescription: String) -> ScoringScale](scoringscale/passfail(passdescription:faildescription:).md)
  Creates a binary pass/fail scoring scale.
- [static func numeric([Double : String]) -> ScoringScale](scoringscale/numeric(_:).md)
  Creates a scoring scale from a numeric dictionary.
- [static func custom<Level>(Level.Type) -> ScoringScale](scoringscale/custom(_:).md)
  Creates a scoring scale from a typed score level enum.
- [init(options: [ScaleOption])](scoringscale/init(options:).md)
  Creates a scoring scale with explicit options.
### Inspecting a scale
- [let options: [ScaleOption]](scoringscale/options.md)
  The scale options, ordered from highest to lowest value.
- [struct ScaleOption](scaleoption.md)
  A single option in a scoring scale.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol ScoreLevel](scorelevel.md)
  A type that defines individual levels within a scoring scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringscale)*