# init(model:tools:instructions:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a session in a blank slate state with an instructions builder.

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

**Other overloads**:

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], instructions: Instructions? = nil)
```

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], instructions: String? = nil)
```

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], instructions: Instructions? = nil)
```

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], instructions: String? = nil)
```

```swift
convenience init<Failure>(model: some LanguageModel, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws(Failure) -> Instructions) throws(Failure) where Failure : Error
```

## Mentions

- [Adding server-side intelligence with Private Cloud Compute](../adding-server-side-intelligence-with-private-cloud-compute.md)
- [Running a Core AI model in a Foundation Models session](../running-a-core-ai-model-in-a-foundation-models-session.md)

## Discussion

- Parameters

  - model: The language model to use for this session.
  - tools: Tools to make available to the model for this session.
  - instructions: Instructions that control the model’s behavior.

## See Also

### Creating a session
- [convenience(model:tools:transcript:)](./init%28model,tools,transcript%29.md)
  Creates a session by rehydrating from a transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:instructions:))*