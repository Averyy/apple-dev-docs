# id

**Framework**: Foundation Models  
**Kind**: property

A unique id that is stable for the duration of a generated response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var id: GenerationID?
```

#### Discussion

A [`LanguageModelSession`](languagemodelsession.md) produces instances of [`GeneratedContent`](generatedcontent.md) that have a non-nil `id`. When you stream a response, the `id` is the same for all partial generations in the response stream.

Instances of [`GeneratedContent`](generatedcontent.md) that you produce manually with initializers have a nil `id` because the framework didn’t create them as part of a generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/id)*