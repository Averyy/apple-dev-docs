# Foundation Models

**Framework**: Foundation Models  
**Kind**: module

Perform tasks with models that specialize in language understanding, structured output, and tool calling.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Mentions

- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)

#### Overview

The Foundation Models framework provides access to any large language model, like the on-device and Private Cloud Compute models designed for Apple Intelligence. These models help you perform intelligent tasks specific to your use case.

![An illustration that represents a foundation model.](https://docs-assets.developer.apple.com/published/b3611fd2257678850b9584e3d05b7438/foundation-models-framework-hero%402x.png)

On-device models excel at a diverse range of text generation tasks, like summarization, entity extraction, text and image understanding, refinement, dialog for games, generating creative content, and more. When you need more reasoning capabilities and context size, use Private Cloud Compute or any server model provider.

The dynamic profile API provides the flexibility to select the best model configuration for your task, and lets you build many useful abstractions, such as agents or skills.

Generate entire Swift data structures with guided generation. With the `@Generable` macro, you can define custom data structures and the framework provides strong guarantees that the model generates instances of your type.

Use [`Tool`](tool.md) to create custom tools that the model can call to assist with handling your request. For example, the model can call a tool that searches a local or online database for information, or calls a service in your app.

To use Apple Foundation Models, people need to turn on Apple Intelligence on their device. For a list of supported devices, see [`Apple Intelligence`](https://developer.apple.comhttps://www.apple.com/apple-intelligence/).

##### Whats New

## Topics

### Essentials
- [Foundation Models updates](../Updates/FoundationModels.md)
  Learn about important changes to Foundation Models.
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
  Enhance the experience in your app by prompting an on-device large language model.
- [Adding intelligent app features with generative models](adding-intelligent-app-features-with-generative-models.md)
  Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.
### Sessions and prompts
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
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.
### Prompt attachments
- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)
  Analyze and extract information from images by combining them with descriptive text prompts.
- [struct Attachment](attachment.md)
  An asset provided to the model.
- [protocol AttachmentContent](attachmentcontent.md)
  A type that you use as the content of an attachment.
- [struct ImageAttachmentContent](imageattachmentcontent.md)
  A type that holds image data.
- [struct ImageReference](imagereference.md)
  A reference to an image in a session’s transcript.
### Dynamic profiles
- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](dynamicinstructions.md)
  A type that represents dynamic instructions.
- [struct DynamicInstructionsForEach](dynamicinstructionsforeach.md)
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.
### Structured output
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [protocol Generable](generable.md)
  A type that the model uses when responding to prompts.
- [struct GenerationSchema](generationschema.md)
  A type that describes the properties of an object and any guides on their values.
- [struct DynamicGenerationSchema](dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.
### Tools
- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)
  Build tools that enable the model to perform tasks that are specific to your use case.
- [Generate dynamic game content with guided generation and tools](generate-dynamic-game-content-with-guided-generation-and-tools.md)
  Make gameplay more lively with AI generated dialog and encounters personalized to the player.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.
### System language model
- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)
  Generate content in the language people prefer when they interact with your app.
- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)
  Identify topics, actions, objects, and emotions in input text with a content tagging model.
- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device Apple Foundation Model capable of text generation tasks.
- [enum LanguageModelError](languagemodelerror.md)
  A failure that may occur while generating a response when using any language model.
### Private Cloud Compute
- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)
  Access a larger context window and stronger reasoning by routing session requests through Private Cloud Compute.
- [com.apple.developer.private-cloud-compute](../BundleResources/Entitlements/com.apple.developer.private-cloud-compute.md)
  A Boolean value that indicates whether the app can use Private Cloud Compute.
- [class PrivateCloudComputeLanguageModel](privatecloudcomputelanguagemodel.md)
  A variant of Apple Foundation Models that runs on Private Cloud Compute (PCC) to provide enhanced capabilities while maintaining privacy guarantees.
### Custom language model provider
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)
  Prevent repeated token processing by preserving the cached state across turns.
- [protocol LanguageModel](languagemodel.md)
  A protocol that you use to interface with a model.
- [struct LanguageModelCapabilities](languagemodelcapabilities.md)
  A set of capabilities that a language model provides.
- [protocol LanguageModelExecutor](languagemodelexecutor.md)
  A protocol that defines the interface for responding to session requests.
- [struct LanguageModelExecutorGenerationChannel](languagemodelexecutorgenerationchannel.md)
  A type you use to send model output deltas and updates to the framework.
- [struct LanguageModelExecutorGenerationRequest](languagemodelexecutorgenerationrequest.md)
  A type that contains the details for a generation request.
### Custom session properties
- [LanguageModelSession.SessionProperty](languagemodelsession/sessionproperty.md)
  A property wrapper that provides access to properties from within profiles,  dynamic instructions, and tools.
- [protocol SessionPropertyKey](sessionpropertykey.md)
  A protocol for defining a custom session property key.
- [class SessionPropertyValues](sessionpropertyvalues.md)
  A container for property values.
- [macro SessionPropertyEntry()](sessionpropertyentry().md)
  A macro for defining a custom key.
### Safety
- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
  Create generative experiences that appropriately handle sensitive inputs and respect people.
### Performance and evaluation
- [Evaluating prompts to measure performance and improve model responses](evaluating-prompts-to-measure-performance-and-improve-model-responses.md)
  Systematically measure and improve the quality of your prompts by using structured evaluation.
- [Evaluating language model responses](../Evaluations/evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.
- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Measure how prompts, responses, and tool calls affect token consumption and response times in Instruments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FoundationModels)*