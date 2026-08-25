# passFail(passDescription:failDescription:)

**Framework**: Evaluations  
**Kind**: method

Creates a binary pass or fail scoring scale.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
static func passFail(passDescription: String, failDescription: String) -> ScoringScale
```

## Parameters

- `passDescription`: Rubric guidance for what constitutes a pass.
- `failDescription`: Rubric guidance for what constitutes a fail.

## See Also

- [static func numeric([Double : String]) -> ScoringScale](scoringscale/numeric(_:).md)
  Creates a scoring scale from a numeric dictionary.
- [static func custom<Level>(Level.Type) -> ScoringScale](scoringscale/custom(_:).md)
  Creates a scoring scale from a typed score level enum.
- [init(options: [ScaleOption])](scoringscale/init(options:).md)
  Creates a scoring scale with explicit options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringscale/passfail(passdescription:faildescription:))*