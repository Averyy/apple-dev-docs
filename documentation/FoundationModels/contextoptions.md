# ContextOptions

**Framework**: Foundation Models  
**Kind**: struct

Options that configure details that should appear in the prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ContextOptions
```

## Mentions

- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)

#### Overview

Create a [`ContextOptions`](contextoptions.md) structure when you need to bias the model’s behavior by adjusting how the model receives your prompt.

## Topics

### Creating context options
- [init(includeSchemaInPrompt: Bool?, reasoningLevel: ContextOptions.ReasoningLevel?)](contextoptions/init(includeschemainprompt:reasoninglevel:).md)
  Creates options that control how the model is prompted.
### Configuring the reasoning level
- [var reasoningLevel: ContextOptions.ReasoningLevel?](contextoptions/reasoninglevel-swift.property.md)
  Controls the amount of reasoning that the model is allowed to output before producing a response.
- [ContextOptions.ReasoningLevel](contextoptions/reasoninglevel-swift.enum.md)
  Controls the amount of reasoning that the model is allowed to output before producing a response.
### Including the schema
- [var includeSchemaInPrompt: Bool?](contextoptions/includeschemainprompt.md)
  A Boolean value that indicates whether to inject the schema into the prompt to bias the model.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/contextoptions)*