# id

**Framework**: Foundation Models  
**Kind**: property

A unique ID used for the duration of a generated response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var id: GenerationID?
```

#### Discussion

A [`LanguageModelSession`](languagemodelsession.md) produces instances of `GeneratedContent` that have a non-nil `id`. When you stream a response, the `id` is the same for all partial generations in the response stream.

Instances of `GeneratedContent` that you produce manually with initializers have a nil `id` because the framework didn’t create them as part of a generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/id)*