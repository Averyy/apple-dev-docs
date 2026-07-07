# init(model:tools:instructions:)

**Framework**: Foundation Models  
**Kind**: init

Start a new session in blank slate state with instructions builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws -> Instructions) rethrows
```

## Mentions

- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)

#### Discussion

- Parameters - model: The language model to use for this session.
- tools: Tools to make available to the model for this session.
- instructions: Instructions that control the model’s behavior.

## See Also

- [convenience(model:tools:transcript:)](languagemodelsession/init(model:tools:transcript:).md)
  Start a session by rehydrating from a transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:instructions:))*