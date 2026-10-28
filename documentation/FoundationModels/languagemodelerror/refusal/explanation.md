# explanation

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The model’s explanation for why it refused to generate a response.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated(nonsending)
var explanation: LanguageModelSession.Response<String> { get async throws }
```

## See Also

### Getting a refusal explanation
- [var explanationStream: LanguageModelSession.ResponseStream<String>](./explanationstream.md)
  The model’s explanation for why it refused to generate a response, delivered as it streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/refusal/explanation)*