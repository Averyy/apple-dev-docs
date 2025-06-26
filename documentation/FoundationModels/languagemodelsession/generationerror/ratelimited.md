# LanguageModelSession.GenerationError.rateLimited(_:)

**Framework**: Foundation Models  
**Kind**: case

An error that indicates your session has been rate limited.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case rateLimited(LanguageModelSession.GenerationError.Context)
```

#### Discussion

This error will only happen if your app is running in the background and exceeds the system defined rate limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/generationerror/ratelimited(_:))*