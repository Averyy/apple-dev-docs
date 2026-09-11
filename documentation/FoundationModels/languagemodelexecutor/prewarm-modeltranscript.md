# prewarm(model:transcript:)

**Framework**: Foundation Models  
**Kind**: method  
**Required**: Yes

Loads assets into memory or pre-fills caches ahead of a request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func prewarm(model: Self.Model, transcript: Transcript)
```

#### Discussion

> **Note**: The default implementation is a no-op.

## See Also

- [associatedtype Model : LanguageModel](languagemodelexecutor/model.md)
  The model type this executor processes requests for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutor/prewarm(model:transcript:))*