# streamResponse(to:options:)

**Framework**: Foundation Models  
**Kind**: method

Produces a response stream to a prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func streamResponse(to prompt: Prompt, options: GenerationOptions = GenerationOptions()) -> sending LanguageModelSession.ResponseStream<String>
```

#### Return Value

A response stream that produces aggregated tokens.

#### Discussion

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelSession.GenerationError.rateLimited(_:)`](languagemodelsession/generationerror/ratelimited(_:).md) errors.

## Parameters

- `prompt`: A specific prompt for the model to respond to.
- `options`: GenerationOptions that control how tokens are sampled from the distribution the model produces.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(to:options:))*