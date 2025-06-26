# Foundation Models

**Framework**: Foundation Models  
**Kind**: module

Perform tasks with the on-device model that specializes in language understanding, structured output, and tool calling.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

#### Overview

The Foundation Models framework provides access to Apple’s on-device large language model that powers Apple Intelligence to help you perform intelligent tasks specific to your use case. The text-based on-device model identifies patterns that allow for generating new text that’s appropriate for the request you make, and it can make decisions to call code you write to perform specialized tasks.

Generate text content based on requests you make. The on-device model excels at a diverse range of text generation tasks, like summarization, entity extraction, text understanding, refinement, dialog for games, generating creative content, and more.

Generate entire Swift data structures with guided generation. With the `@Generable` macro, you can define custom data structures and the framework provides strong guarantees that the model generates instances of your type.

To expand what the on-device foundation model can do, use [`Tool`](tool.md) to create custom tools that the model can call to assist with handling your request. For example, the model can call a tool that searches a local or online database for information, or calls a service in your app.

To use the on-device language model, people need to turn on Apple Intelligence on their device. For a list of supported devices, see [`Apple Intelligence`](https://developer.apple.comhttps://www.apple.com/apple-intelligence/).

For more information about acceptable usage of the Foundation Models framework, see [`Acceptable use requirements for the Foundation Models framework`](https://developer.apple.comhttps://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework).

## Topics

### Essentials
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
  Enhance the experience in your app by prompting an on-device large language model.
- [Improving safety from generative model output](improving-safety-from-generative-model-output.md)
  Create generative experiences that appropriately handle sensitive inputs and respect people.
- [Adding intelligent app features with generative models](adding-intelligent-app-features-with-generative-models.md)
  Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.
- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.
- [SystemLanguageModel.UseCase](systemlanguagemodel/usecase.md)
  A type that represents the use case for prompting.
### Prompting
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a large language model.
- [struct Instructions](instructions.md)
  Instructions define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model. Transcripts contain an ordered list of entries, representing inputs to and outputs from the model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
### Guided generation
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [protocol Generable](generable.md)
  A type that the model uses when responding to prompts.
### Tool calling
- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)
  Build tools that enable the model to perform tasks that are specific to your use case.
- [Generate dynamic game content with guided generation and tools](generate-dynamic-game-content-with-guided-generation-and-tools.md)
  Make gameplay more lively with AI generated dialog and encounters personalized to the player.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.
### Feedback
- [struct LanguageModelFeedbackAttachment](languagemodelfeedbackattachment.md)
  Feedback appropriate for attaching to Feedback Assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FoundationModels)*