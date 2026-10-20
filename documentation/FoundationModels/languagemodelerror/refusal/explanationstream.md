# explanationStream

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The model’s explanation for why it refused to generate a response, delivered as it streams.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var explanationStream: LanguageModelSession.ResponseStream<String> { get }
```

## See Also

### Getting a refusal explanation
- [var explanation: LanguageModelSession.Response<String>](./explanation.md)
  The model’s explanation for why it refused to generate a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/refusal/explanationstream)*