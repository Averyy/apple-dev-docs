# passFail(passDescription:failDescription:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a binary pass or fail scoring scale.

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
static func passFail(passDescription: String, failDescription: String) -> ScoringScale
```

## Parameters

- `passDescription`: Rubric guidance for what constitutes a pass.
- `failDescription`: Rubric guidance for what constitutes a fail.

## See Also

### Creating a scale
- [static func numeric([Double : String]) -> ScoringScale](./numeric%28_%29.md)
  Creates a scoring scale from a numeric dictionary.
- [static func custom<Level>(Level.Type) -> ScoringScale](./custom%28_%29.md)
  Creates a scoring scale from a typed score level enum.
- [init(options: [ScaleOption])](./init%28options%29.md)
  Creates a scoring scale with explicit options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringscale/passfail(passdescription:faildescription:))*