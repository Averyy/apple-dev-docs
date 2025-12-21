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

#### Discussion

- Parameters - model: The language model to use for this session.
- tools: Tools to make available to the model for this session.
- instructions: Instructions that control the model’s behavior.

## See Also

- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:instructions:))*