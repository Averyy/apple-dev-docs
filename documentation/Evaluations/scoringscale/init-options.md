# init(options:)

**Framework**: Evaluations  
**Kind**: init

Creates a scoring scale with explicit options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(options: [ScaleOption])
```

## Parameters

- `options`: The scale options. Sorted by value descending.

## See Also

- [static func passFail(passDescription: String, failDescription: String) -> ScoringScale](scoringscale/passfail(passdescription:faildescription:).md)
  Creates a binary pass/fail scoring scale.
- [static func numeric([Double : String]) -> ScoringScale](scoringscale/numeric(_:).md)
  Creates a scoring scale from a numeric dictionary.
- [static func custom<Level>(Level.Type) -> ScoringScale](scoringscale/custom(_:).md)
  Creates a scoring scale from a typed score level enum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoringscale/init(options:))*