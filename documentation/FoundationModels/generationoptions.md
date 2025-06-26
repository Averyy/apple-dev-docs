# GenerationOptions

**Framework**: Foundation Models  
**Kind**: struct

Options that control how the model generates its response to a prompt.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct GenerationOptions
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

#### Overview

Create a [`GenerationOptions`](generationoptions.md) structure when you want to adjust the way the model generates its response. Use this structure to perform various adjustments on how the model chooses output tokens, to specify the penalties for repeating tokens or generating longer responses.

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
### Comparing generation options
- [static func == (GenerationOptions, GenerationOptions) -> Bool](generationoptions/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](generationoptions/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a large language model.
- [struct Instructions](instructions.md)
  Instructions define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model. Transcripts contain an ordered list of entries, representing inputs to and outputs from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions)*