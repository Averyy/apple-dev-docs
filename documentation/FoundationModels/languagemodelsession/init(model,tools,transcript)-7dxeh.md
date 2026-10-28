# init(model:tools:transcript:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a session that resumes from an existing transcript.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], transcript: Transcript)
```

**Other overloads**:

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], transcript: Transcript)
```

## Parameters

- `model`: The language model the session uses to generate responses.
- `tools`: The tools the model can call while responding.
- `transcript`: The transcript of a conversation to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:transcript:)-7dxeh)*