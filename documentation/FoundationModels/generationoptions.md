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

## Declaration

```swift
struct GenerationOptions
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

#### Overview

Generation options determine the decoding strategy the framework uses to adjust the way the model chooses output tokens. When you interact with the model, it converts your input to a token sequence, and uses it to generate the response.

Only use [`maximumResponseTokens`](generationoptions/maximumresponsetokens.md) when you need to protect against unexpectedly verbose responses. Enforcing a strict token response limit can lead to the model producing malformed results or gramatically incorrect responses.

All input to the model contributes tokens to the context window of the [`LanguageModelSession`](languagemodelsession.md) — including the [`Instructions`](instructions.md), [`Prompt`](prompt.md), [`Tool`](tool.md), and [`Generable`](generable.md) types, and the model’s responses. If your session exceeds the available context size, it throws [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md). For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

## Topics

### Creating options
- [init(sampling: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](generationoptions/init(sampling:temperature:maximumresponsetokens:).md)
  Creates generation options that control token sampling behavior.
### Configuring the response tokens
- [var maximumResponseTokens: Int?](generationoptions/maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.
### Configuring the sampling mode
- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [GenerationOptions.SamplingMode](generationoptions/samplingmode.md)
  A type that defines how values are sampled from a probability distribution.
### Configuring the temperature
- [var temperature: Double?](generationoptions/temperature.md)
  Temperature influences the confidence of the models response.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions)*