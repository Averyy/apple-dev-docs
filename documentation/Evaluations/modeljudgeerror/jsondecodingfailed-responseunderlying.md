# ModelJudgeError.jsonDecodingFailed(response:underlying:)

**Framework**: Evaluations  
**Kind**: case

The evaluator fails to decode the JSON from the model judge’s response.

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
case jsonDecodingFailed(response: String, underlying: any Error)
```

## Parameters

- `response`: The raw response text from the model judge.
- `underlying`: The decoding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror/jsondecodingfailed(response:underlying:))*