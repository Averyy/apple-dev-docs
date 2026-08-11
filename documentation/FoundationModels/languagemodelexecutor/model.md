# Model

**Framework**: Foundation Models  
**Kind**: associatedtype  
**Required**: Yes

The model type this executor processes requests for.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Model : LanguageModel
```

## See Also

- [func prewarm(model: Self.Model, transcript: Transcript)](languagemodelexecutor/prewarm(model:transcript:).md)
  Loads assets into memory or pre-fills caches ahead of a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutor/model)*