# historyTransform(_:)

**Framework**: Foundation Models  
**Kind**: method

Applies a transformation to the history prior to invoking the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func historyTransform(_ transform: @escaping ([Transcript.Entry]) -> [Transcript.Entry]) -> some LanguageModelSession.DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/historytransform(_:))*