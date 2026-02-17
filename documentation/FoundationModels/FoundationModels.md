# Foundation Models

**Framework**: Foundation Models  
**Kind**: module

Perform tasks with the on-device model that specializes in language understanding, structured output, and tool calling.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Mentions

- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)

#### Overview

The Foundation Models framework provides access to Apple’s on-device large language model that powers Apple Intelligence to help you perform intelligent tasks specific to your use case. The text-based on-device model identifies patterns that allow for generating new text that’s appropriate for the request you make, and it can make decisions to call code you write to perform specialized tasks.

![An illustration that represents a foundation model.](https://docs-assets.developer.apple.com/published/274bdf69903b6dd606f05b29f5e08f04/foundation-models-framework-hero%402x.png)

Generate text content based on requests you make. The on-device model excels at a diverse range of text generation tasks, like summarization, entity extraction, text understanding, refinement, dialog for games, generating creative content, and more.

Generate entire Swift data structures with guided generation. With the `@Generable` macro, you can define custom data structures and the framework provides strong guarantees that the model generates instances of your type.

To expand what the on-device foundation model can do, use [`Tool`](tool.md) to create custom tools that the model can call to assist with handling your request. For example, the model can call a tool that searches a local or online database for information, or calls a service in your app.

To use the on-device language model, people need to turn on Apple Intelligence on their device. For a list of supported devices, see [`Apple Intelligence`](https://developer.apple.comhttps://www.apple.com/apple-intelligence/).

For more information about acceptable usage of the Foundation Models framework, see [`Acceptable use requirements for the Foundation Models framework`](https://developer.apple.comhttps://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework).

##### Related Videos

## Topics

### Essentials
- [Foundation Models updates](../Updates/FoundationModels.md)
  Learn about important changes to Foundation Models.
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
  Enhance the experience in your app by prompting an on-device large language model.
- [Adding intelligent app features with generative models](adding-intelligent-app-features-with-generative-models.md)
  Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.
- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.
### Prompting
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [Evaluating prompts to measure performance and improve model responses](evaluating-prompts-to-measure-performance-and-improve-model-responses.md)
  Systematically measure and improve the quality of your prompts by using structured evaluation.
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
### Safety
- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
  Create generative experiences that appropriately handle sensitive inputs and respect people.
- [SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails.md)
  Guardrails flag sensitive content from model input and output.
### Language and locales
- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)
  Generate content in the language people prefer when they interact with your app.
- [func supportsLocale(Locale) -> Bool](systemlanguagemodel/supportslocale(_:).md)
  Returns a Boolean indicating whether the given locale is supported by the model.
- [case unsupportedLanguageOrLocale(LanguageModelSession.GenerationError.Context)](languagemodelsession/generationerror/unsupportedlanguageorlocale(_:).md)
  An error that indicates an error that occurs if the model is prompted to respond in a language that it does not support.
### Use cases
- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)
  Identify topics, actions, objects, and emotions in input text with a content tagging model.
- [SystemLanguageModel.UseCase](systemlanguagemodel/usecase.md)
  A type that represents the use case for prompting.
### Feedback
- [struct LanguageModelFeedback](languagemodelfeedback.md)
  Feedback appropriate for logging or attaching to Feedback Assistant.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes data that includes session information that you attach when reporting feedback to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FoundationModels)*