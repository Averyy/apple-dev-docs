# streamResponse(generating:includeSchemaInPrompt:options:prompt:)

**Framework**: Foundation Models  
**Kind**: method

Produces a response stream for a type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func streamResponse<Content>(generating type: Content.Type = Content.self, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions(), @PromptBuilder prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content> where Content : Generable
```

## Mentions

- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)

#### Return Value

A response stream.

#### Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelSession.GenerationError.rateLimited(_:)`](languagemodelsession/generationerror/ratelimited(_:).md) errors.

## Parameters

- `type`: A type to produce as the response.
- `includeSchemaInPrompt`: Inject the schema into the prompt to bias the model.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `prompt`: A prompt for the model to respond to.

## See Also

- [func streamResponse(to:options:)](languagemodelsession/streamresponse(to:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:generating:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:schema:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:schema:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:))*