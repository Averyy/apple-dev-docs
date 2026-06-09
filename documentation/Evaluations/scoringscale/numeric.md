# numeric(_:)

**Framework**: Evaluations  
**Kind**: method

Creates a scoring scale from a numeric dictionary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func numeric(_ scale: [Double : String]) -> ScoringScale
```

#### Discussion

Each key-value pair maps a numeric score to rubric guidance. The label for each option is derived from the numeric value (e.g., `5` becomes `"5"`).

## Parameters

- `scale`: A dictionary mapping numeric scores to rubric guidance.

## See Also

- [static func passFail(passDescription: String, failDescription: String) -> ScoringScale](scoringscale/passfail(passdescription:faildescription:).md)
  Creates a binary pass/fail scoring scale.
- [static func custom<Level>(Level.Type) -> ScoringScale](scoringscale/custom(_:).md)
  Creates a scoring scale from a typed score level enum.
- [init(options: [ScaleOption])](scoringscale/init(options:).md)
  Creates a scoring scale with explicit options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringscale/numeric(_:))*