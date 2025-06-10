# init(model:guardrails:tools:instructions:)

**Framework**: Foundation Models  
**Kind**: init

Start a new session in blank slate state with instructions builder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, guardrails: LanguageModelSession.Guardrails = .default, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws -> Instructions) rethrows
```

#### Discussion

- Parameters - model: The language model to use for this session.
- guardrails: Controls the guardrails setting for prompt and response filtering. System guardrails is enabled if not specified.
- tools: Tools to make available to the model for this session.
- instructions: Instructions that control the model’s behavior.

## See Also

- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.
- [LanguageModelSession.Guardrails](languagemodelsession/guardrails.md)
  Guardrails flag sensitive content from model input and output.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.
- [struct Instructions](instructions.md)
  Instructions define the model’s intended behavior on prompts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:guardrails:tools:instructions:))*