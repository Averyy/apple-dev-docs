# init(model:guardrails:tools:transcript:)

**Framework**: Foundation Models  
**Kind**: init

Start a session by rehydrating from a transcript.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, guardrails: LanguageModelSession.Guardrails = .default, tools: [any Tool] = [], transcript: Transcript)
```

#### Discussion

- Parameters - model: The language model to use for this session.
- guardrails: Controls the guardrails setting for prompt and response filtering. System guardrails is enabled if not specified.
- transcript: A transcript to resume from.
- tools: Tools to make available to the model for this session.

## See Also

- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:guardrails:tools:transcript:))*