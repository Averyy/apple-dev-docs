# init(model:tools:transcript:)

**Framework**: Foundation Models  
**Kind**: init

Start a session by rehydrating from a transcript.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], transcript: Transcript)
```

## Mentions

- [Managing the context window](managing-the-context-window.md)
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)

#### Discussion

- Parameters - model: The language model to use for this session.
- transcript: A transcript to resume from.
- tools: Tools to make available to the model for this session.

## See Also

- [convenience(model:tools:instructions:)](languagemodelsession/init(model:tools:instructions:).md)
  Start a new session in blank slate state with instructions builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:transcript:))*