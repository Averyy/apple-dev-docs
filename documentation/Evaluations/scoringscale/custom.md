# custom(_:)

**Framework**: Evaluations  
**Kind**: method

Creates a scoring scale from a typed score level enum.

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
static func custom<Level>(_ level: Level.Type) -> ScoringScale where Level : ScoreLevel
```

#### Discussion

The method enumerates all cases and converts them to [`ScaleOption`](scaleoption.md) values.

## Parameters

- `level`: The score level type.

## See Also

- [static func passFail(passDescription: String, failDescription: String) -> ScoringScale](scoringscale/passfail(passdescription:faildescription:).md)
  Creates a binary pass or fail scoring scale.
- [static func numeric([Double : String]) -> ScoringScale](scoringscale/numeric(_:).md)
  Creates a scoring scale from a numeric dictionary.
- [init(options: [ScaleOption])](scoringscale/init(options:).md)
  Creates a scoring scale with explicit options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringscale/custom(_:))*