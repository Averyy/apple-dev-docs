# ModelJudgeError.jsonDecodingFailed(response:underlying:)

**Framework**: Evaluations  
**Kind**: case

The evaluator fails to decode the JSON from the model judge’s response.

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
case jsonDecodingFailed(response: String, underlying: any Error)
```

## Parameters

- `response`: The raw response text from the model judge.
- `underlying`: The decoding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror/jsondecodingfailed(response:underlying:))*