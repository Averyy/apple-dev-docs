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

## Declaration

```swift
final class LanguageModelSession
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)

#### Overview

A session is a single context that you use to generate content with, and maintains state between requests. You can reuse the existing instance or create a new one each time you call the model. When creating a session, provide instructions that tells the model what its role is and provide guidance on how to respond.

```swift
let instructions = """
    You are a motivational workout coach that provides quotes to inspire \
    and motivate athletes.
    """
let session = LanguageModelSession(instructions: instructions)
let prompt = "Generate a motivational quote for my next workout."
let response = try await session.respond(to: prompt)
```

The framework records each call to the model in a [`Transcript`](transcript.md) that includes all prompts and responses. If your session exceeds the available context size, it throws [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md).

When you perform a task that needs a larger context size, split the task into smaller steps and run each of them in a new [`LanguageModelSession`](languagemodelsession.md). For example, to generate a summary for a long article on device:

1. Separate the article into smaller sections.
2. Summarize each section with a new session instance.
3. Combine the sections.
4. Repeat the steps until you get a summary with the size you want, and consider adding the summary to the prompt so it conveys the contextual information.

Use Instruments to analyze token consumption while your app is running and to look for opportunities to improve performance, like with [`prewarm(promptPrefix:)`](languagemodelsession/prewarm(promptprefix:).md). To profile your app with Instruments:

1. Open your Xcode project and choose Product > Profile to launch Instruments.
2. Select the Blank template, then click Choose.
3. In Instruments, click “+ Instrument” to open the instruments library.
4. Choose the Foundation Models instrument from the list.
5. Choose File > Record Trace. This launches your app and starts a recording session to observe token usage from your app’s model interactions.

Because some generation tasks can be resource intensive, consider profiling your app with other instruments — like Activity Monitor and Power Profiler — to identify where your app might be using more system resources than expected.

For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

## Topics

### Creating a session
- [convenience(model:tools:instructions:)](languagemodelsession/init(model:tools:instructions:).md)
  Start a new session in blank slate state with instructions builder.
- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
### Creating a session from a transcript
- [convenience init(model: SystemLanguageModel, tools: [any Tool], transcript: Transcript)](languagemodelsession/init(model:tools:transcript:).md)
  Start a session by rehydrating from a transcript.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
### Preloading the model
- [func prewarm(promptPrefix: Prompt?)](languagemodelsession/prewarm(promptprefix:).md)
  Loads the resources required for this session into memory, and optionally caches a prefix of your prompt to reduce request latency.
### Inspecting session properties
- [var isResponding: Bool](languagemodelsession/isresponding.md)
  A Boolean value that indicates a response is being generated.
- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.
### Generating a request
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
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [LanguageModelSession.Response](languagemodelsession/response.md)
  A structure that stores the output of a response call.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
### Streaming a response
- [func streamResponse(to:options:)](languagemodelsession/streamresponse(to:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:generating:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:schema:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:schema:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:).md)
  Produces a response stream for a type.
- [func streamResponse(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:includeschemainprompt:options:prompt:).md)
  Produces a response stream to a prompt and schema.
- [LanguageModelSession.ResponseStream](languagemodelsession/responsestream.md)
  An async sequence of snapshots of partially generated content.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
### Generating feedback
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes data that includes session information that you attach when reporting feedback to Apple.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseContent: (any ConvertibleToGeneratedContent)?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:).md)
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseText: String?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:).md)
### Getting the error types
- [LanguageModelSession.GenerationError](languagemodelsession/generationerror.md)
  An error that may occur while generating a response.
- [LanguageModelSession.ToolCallError](languagemodelsession/toolcallerror.md)
  An error that occurs while a system language model is calling a tool.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession)*