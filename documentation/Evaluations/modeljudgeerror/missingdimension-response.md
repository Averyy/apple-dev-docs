# ModelJudgeError.missingDimension(_:response:)

**Framework**: Evaluations  
**Kind**: case

The model judge’s response is missing a required scoring dimension. The first associated value is the name of the missing dimension.

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
case missingDimension(String, response: String)
```

## Parameters

- `response`: The raw response text from the model judge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror/missingdimension(_:response:))*