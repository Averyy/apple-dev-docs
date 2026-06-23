# GenerationOptions

**Framework**: Foundation Models  
**Kind**: struct

Options that control how the model generates its response to a prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct GenerationOptions
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

#### Overview

Generation options determine the decoding strategy the framework uses to adjust the way the model chooses output tokens. When you interact with the model, it converts your input to a token sequence, and uses it to generate the response.

Only use [`maximumResponseTokens`](generationoptions/maximumresponsetokens.md) when you need to protect against unexpectedly verbose responses. Enforcing a strict token response limit can lead to the model producing malformed results or grammatically incorrect responses.

All input to the model contributes tokens to the context window of the [`LanguageModelSession`](languagemodelsession.md) — including the [`Instructions`](instructions.md), [`Prompt`](prompt.md), [`Tool`](tool.md), and [`Generable`](generable.md) types, and the model’s responses. If your session exceeds the available context size, it throws [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md). For more information on managing the context window size, see [`Managing the context window`](managing-the-context-window.md).

## Topics

### Creating options
- [init(samplingMode: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](generationoptions/init(samplingmode:temperature:maximumresponsetokens:).md)
- [init(samplingMode: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?, toolCallingMode: GenerationOptions.ToolCallingMode?)](generationoptions/init(samplingmode:temperature:maximumresponsetokens:toolcallingmode:).md)
  Creates generation options that control token sampling behavior.
- [init(sampling: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](generationoptions/init(sampling:temperature:maximumresponsetokens:).md)
  Creates generation options that control token sampling behavior.
### Configuring options
- [var temperature: Double?](generationoptions/temperature.md)
  Temperature influences the confidence of the models response.
- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](generationoptions/samplingmode-swift.property.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct.md)
  A type that defines how values are sampled from a probability distribution.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](generationoptions/toolcallingmode-swift.property.md)
  Configure the tool calling requirements.
- [GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct.md)
  A value you use to describe the model behavior when it comes to tool usage.
- [var maximumResponseTokens: Int?](generationoptions/maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Managing the context window](managing-the-context-window.md)
  Optimize your app’s token usage when prompting a model with the Foundation Models framework.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct TranscriptErrorHandlingPolicy](transcripterrorhandlingpolicy.md)
  Options for controlling how a language model session manages the transcript when errors occur.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions)*