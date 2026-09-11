# ModelJudgeError.missingDimension(_:response:)

**Framework**: Evaluations  
**Kind**: case

The model judge’s response is missing a required scoring dimension. The first associated value is the name of the missing dimension.

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
case missingDimension(String, response: String)
```

## Parameters

- `response`: The raw response text from the model judge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror/missingdimension(_:response:))*