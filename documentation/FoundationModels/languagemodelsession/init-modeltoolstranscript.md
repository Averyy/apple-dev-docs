# init(model:tools:transcript:)

**Framework**: Foundation Models  
**Kind**: init

Creates a session by rehydrating from a transcript.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], transcript: Transcript)
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)
- [Managing the context window](managing-the-context-window.md)
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)

#### Discussion

- Parameters - model: The language model to use for this session.
- transcript: A transcript to resume from.
- tools: Tools to make available to the model for this session.

## See Also

- [convenience(model:tools:instructions:)](languagemodelsession/init(model:tools:instructions:).md)
  Creates a session in a blank slate state with an instructions builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:transcript:))*