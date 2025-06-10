# collect(isolation:)

**Framework**: Foundation Models  
**Kind**: method

The result from a streaming response, after it completes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func collect(isolation actor: isolated (any Actor)? = #isolation) async throws -> sending LanguageModelSession.Response<Content>
```

#### Discussion

If the streaming response was finished successfully before calling `collect()`, this method `Response` returns immediately.

If the streaming response was finished with an error before calling `collect()`, this method propagates that error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/collect(isolation:))*