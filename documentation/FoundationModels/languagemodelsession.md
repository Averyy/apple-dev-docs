# LanguageModelSession

**Framework**: Foundation Models  
**Kind**: class

An object that represents a session that interacts with a language model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
final class LanguageModelSession
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)
- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)
- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
- [Managing the context window](managing-the-context-window.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
- [Running a Core AI model in a Foundation Models session](running-a-core-ai-model-in-a-foundation-models-session.md)
- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)

#### Overview

A session is a single context that you use to generate content with, and maintains state between requests. You can reuse the existing instance or create a new one each time you call the model. When you create a session you can provide instructions that tells the model what its role is and provides guidance on how to respond.

```swift
let session = LanguageModelSession(instructions: """
    You are a motivational workout coach that provides quotes to inspire \
    and motivate athletes.
    """
)
let prompt = "Generate a motivational quote for my next workout."
let response = try await session.respond(to: prompt)
```

The framework records each call to the model in a [`Transcript`](transcript.md) that includes all prompts and responses. If your session exceeds the available context size, it throws [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md). For more information on managing the context window size, see [`Managing the context window`](managing-the-context-window.md).

Use Instruments to analyze token consumption while your app is running and to look for opportunities to improve performance, like with [`prewarm(promptPrefix:)`](languagemodelsession/prewarm(promptprefix:).md). For more information on Instruments, see [`Analyzing the runtime performance of your Foundation Models app`](analyzing-the-runtime-performance-of-your-foundation-models-app.md).

## Topics

### Creating a session
- [convenience(model:tools:instructions:)](languagemodelsession/init(model:tools:instructions:).md)
  Creates a session in a blank slate state with an instructions builder.
- [convenience(model:tools:transcript:)](languagemodelsession/init(model:tools:transcript:).md)
  Creates a session by rehydrating from a transcript.
### Creating a session with a dynamic profile
- [convenience init(profile: sending some LanguageModelSession.DynamicProfile, history: some Collection<Transcript.Entry>)](languagemodelsession/init(profile:history:).md)
  Creates a session with a profile.
- [convenience init(model: some LanguageModel, dynamicInstructions: sending some DynamicInstructions, history: some Collection<Transcript.Entry>)](languagemodelsession/init(model:dynamicinstructions:history:).md)
  Creates a session with dynamic instructions.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.ConditionalDynamicProfile](languagemodelsession/conditionaldynamicprofile.md)
- [LanguageModelSession.DynamicProfileBuilder](languagemodelsession/dynamicprofilebuilder.md)
  A type that represents a dynamic profile builder.
- [LanguageModelSession.DynamicProfileModifierContent](languagemodelsession/dynamicprofilemodifiercontent.md)
- [LanguageModelSession.ModifiedDynamicProfile](languagemodelsession/modifieddynamicprofile.md)
- [LanguageModelSession.AnyDynamicProfile](languagemodelsession/anydynamicprofile.md)
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.
### Preloading the model
- [func prewarm(promptPrefix: Prompt?)](languagemodelsession/prewarm(promptprefix:).md)
  Loads the resources required for this session into memory ahead of a request.
### Accessing session properties
- [var properties: SessionPropertyValues](languagemodelsession/properties.md)
### Inspecting the accumulated usage
- [var usage: LanguageModelSession.Usage](languagemodelsession/usage-swift.property.md)
  The total accumulated usage across all responses generated by this session.
- [LanguageModelSession.Usage](languagemodelsession/usage-swift.struct.md)
  Information about how many tokens were used by a response.
### Configuring the transcript error handling policy
- [var transcriptErrorHandlingPolicy: TranscriptErrorHandlingPolicy?](languagemodelsession/transcripterrorhandlingpolicy.md)
  The session’s policy for managing the transcript when errors occur.
- [struct TranscriptErrorHandlingPolicy](transcripterrorhandlingpolicy.md)
  Options for controlling how a language model session manages the transcript when errors occur.
### Generating a response
- [var isResponding: Bool](languagemodelsession/isresponding.md)
  A Boolean value that indicates whether a response is being generated.
- [func respond(options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>](languagemodelsession/respond(options:prompt:).md)
  Produces a response to a prompt.
- [func respond<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<Content>](languagemodelsession/respond(generating:includeschemainprompt:options:prompt:).md)
  Produces a generable object as a response to a prompt.
- [func respond(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](languagemodelsession/respond(schema:includeschemainprompt:options:prompt:).md)
  Produces a generated content type as a response to a prompt and schema.
- [func respond(to:options:)](languagemodelsession/respond(to:options:).md)
  Produces a response to a prompt.
- [func respond(to:generating:includeSchemaInPrompt:options:)](languagemodelsession/respond(to:generating:includeschemainprompt:options:).md)
  Produces a generable object as a response to a prompt.
- [func respond(to:schema:includeSchemaInPrompt:options:)](languagemodelsession/respond(to:schema:includeschemainprompt:options:).md)
  Produces a generated content type as a response to a prompt and schema.
- [LanguageModelSession.Response](languagemodelsession/response.md)
  A structure that stores the output of a response call.
### Generating a response with metadata
- [func respond(options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>](languagemodelsession/respond(options:contextoptions:metadata:prompt:).md)
  Produces a response to a prompt.
- [func respond<Content>(generating: Content.Type, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<Content>](languagemodelsession/respond(generating:options:contextoptions:metadata:prompt:).md)
  Produces a generable object as a response to a prompt.
- [func respond(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](languagemodelsession/respond(schema:options:contextoptions:metadata:prompt:).md)
  Produces a generated content type as a response to a prompt and schema.
- [func respond(to:options:contextOptions:metadata:)](languagemodelsession/respond(to:options:contextoptions:metadata:).md)
  Produces a response to a prompt.
- [func respond(to:generating:options:contextOptions:metadata:)](languagemodelsession/respond(to:generating:options:contextoptions:metadata:).md)
  Produces a generable object as a response to a prompt.
- [func respond(to:schema:options:contextOptions:metadata:)](languagemodelsession/respond(to:schema:options:contextoptions:metadata:).md)
  Produces a generated content type as a response to a prompt and schema.
### Streaming a response
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:includeschemainprompt:options:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:options:)](languagemodelsession/streamresponse(to:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:generating:includeschemainprompt:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:schema:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [LanguageModelSession.ResponseStream](languagemodelsession/responsestream.md)
  An async sequence of snapshots of partially generated content.
### Streaming a response with metadata
- [func streamResponse(options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:generating:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:schema:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt and schema.
### Accessing the transcript
- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.
### Generating feedback
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes a feedback attachment that can be submitted to Apple.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseContent: (any ConvertibleToGeneratedContent)?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:).md)
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseText: String?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:).md)
- [struct LanguageModelFeedback](languagemodelfeedback.md)
  Feedback appropriate for logging or attaching to Feedback Assistant.
### Session properties
- [LanguageModelSession.SessionProperty](languagemodelsession/sessionproperty.md)
  A property wrapper that provides access to properties from within profiles,  dynamic instructions, and tools.
### Errors
- [LanguageModelSession.Error](languagemodelsession/error.md)
  A failure caused by incorrect use of a language model session.
- [LanguageModelSession.ToolCallError](languagemodelsession/toolcallerror.md)
  An error that occurs while a language model is calling a tool.
- [LanguageModelSession.GenerationError](languagemodelsession/generationerror.md)
  An error that may occur while generating a response.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Managing the context window](managing-the-context-window.md)
  Optimize your app’s token usage when prompting a model with the Foundation Models framework.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession)*