# LanguageModelSession

**Framework**: Foundation Models  
**Kind**: class

An object that represents a session that interacts with a large language model.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class LanguageModelSession
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

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

The framework records each call to the model in a [`Transcript`](transcript.md) that includes all prompts and responses. If your session exceeds the available context size, it throws an [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md)

## Topics

### Creating a session
- [convenience(model:guardrails:tools:instructions:)](languagemodelsession/init(model:guardrails:tools:instructions:).md)
  Start a new session in blank slate state with instructions builder.
- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.
- [LanguageModelSession.Guardrails](languagemodelsession/guardrails.md)
  Guardrails flag sensitive content from model input and output.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.
- [struct Instructions](instructions.md)
  Instructions define the model’s intended behavior on prompts.
### Creating a session from a transcript
- [convenience init(model: SystemLanguageModel, guardrails: LanguageModelSession.Guardrails, tools: [any Tool], transcript: Transcript)](languagemodelsession/init(model:guardrails:tools:transcript:).md)
  Start a session by rehydrating from a transcript.
- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model.
### Preloading the model
- [func prewarm()](languagemodelsession/prewarm.md)
  Requests that the system eagerly load the resources required for this session into memory.
### Inspecting session properties
- [var isResponding: Bool](languagemodelsession/isresponding.md)
  A Boolean value that indicates a response is being generated.
- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.
- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.
### Generating a request
- [func respond<Content>(generating: Content.Type, options: GenerationOptions, includeSchemaInPrompt: Bool, isolation: isolated (any Actor)?, prompt: () throws -> Prompt) async throws -> sending LanguageModelSession.Response<Content>](languagemodelsession/respond(generating:options:includeschemainprompt:isolation:prompt:).md)
  Produces a generable object as a response to a prompt.
- [func respond(options: GenerationOptions, isolation: isolated (any Actor)?, prompt: () throws -> Prompt) async throws -> sending LanguageModelSession.Response<String>](languagemodelsession/respond(options:isolation:prompt:).md)
  Produces a response to a prompt.
- [func respond(options: GenerationOptions, schema: GenerationSchema, includeSchemaInPrompt: Bool, isolation: isolated (any Actor)?, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](languagemodelsession/respond(options:schema:includeschemainprompt:isolation:prompt:).md)
  Produces a generated content type as a response to a prompt and schema.
- [func respond(to:generating:includeSchemaInPrompt:options:isolation:)](languagemodelsession/respond(to:generating:includeschemainprompt:options:isolation:).md)
  Produces a generable object as a response to a prompt.
- [func respond(to:options:isolation:)](languagemodelsession/respond(to:options:isolation:).md)
  Produces a response to a prompt.
- [func respond(to:schema:includeSchemaInPrompt:options:isolation:)](languagemodelsession/respond(to:schema:includeschemainprompt:options:isolation:).md)
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
- [func streamResponse<Content>(generating: Content.Type, options: GenerationOptions, includeSchemaInPrompt: Bool, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:options:includeschemainprompt:prompt:).md)
  Produces a response stream for a type.
- [func streamResponse(options: GenerationOptions, schema: GenerationSchema, includeSchemaInPrompt: Bool, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(options:schema:includeschemainprompt:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
- [LanguageModelSession.ResponseStream](languagemodelsession/responsestream.md)
  A structure that  stores the output of a response stream.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
### Getting the error types
- [LanguageModelSession.GenerationError](languagemodelsession/generationerror.md)
  An error that occurs while generating a response.
- [LanguageModelSession.ToolCallError](languagemodelsession/toolcallerror.md)
  An error that occurs while a system language model is calling a tool.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Instructions](instructions.md)
  Instructions define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession)*