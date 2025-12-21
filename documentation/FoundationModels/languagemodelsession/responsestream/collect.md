# collect()

**Framework**: Foundation Models  
**Kind**: method

The result from a streaming response, after it completes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func collect() async throws -> sending LanguageModelSession.Response<Content>
```

#### Discussion

If the streaming response was finished successfully before calling `collect()`, this method `Response` returns immediately.

If the streaming response was finished with an error before calling `collect()`, this method propagates that error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/collect())*