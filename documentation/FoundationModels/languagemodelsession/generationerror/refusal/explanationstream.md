# explanationStream

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

A stream containing an explanation about why the model refused to respond.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var explanationStream: LanguageModelSession.ResponseStream<String> { get }
```

## See Also

### Getting the explanation
- [var explanation: LanguageModelSession.Response<String>](./explanation.md)
  An explanation for why the model refused to respond.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/generationerror/refusal/explanationstream)*