# ModelJudgeError.invalidScore(dimension:value:)

**Framework**: Evaluations  
**Kind**: case

A scoring dimension returns a value the evaluator can’t parse as a number.

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
case invalidScore(dimension: String, value: String)
```

## Parameters

- `dimension`: The name of the scoring dimension.
- `value`: The unparsable value the model returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror/invalidscore(dimension:value:))*