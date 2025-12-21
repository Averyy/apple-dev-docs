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

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], transcript: Transcript)
```

#### Discussion

- Parameters - model: The language model to use for this session.
- transcript: A transcript to resume from.
- tools: Tools to make available to the model for this session.

## See Also

- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:transcript:))*