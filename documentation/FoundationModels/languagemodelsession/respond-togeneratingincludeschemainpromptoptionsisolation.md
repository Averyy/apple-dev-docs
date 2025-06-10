# respond(to:generating:includeSchemaInPrompt:options:isolation:)

**Framework**: Foundation Models  
**Kind**: method

Produces a generable object as a response to a prompt.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
final func respond<Content>(to prompt: Prompt, generating type: Content.Type = Content.self, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions(), isolation: isolated (any Actor)? = #isolation) async throws -> sending LanguageModelSession.Response<Content> where Content : Generable
```

#### Return Value

[`GeneratedContent`](generatedcontent.md) containing the fields and values defined in the schema.

#### Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `type`: A type to produce as the response.
- `includeSchemaInPrompt`: Inject the schema into the prompt to bias the model.
- `options`: Options that control how tokens are sampled from the distribution the model produces.

## See Also

- [func respond<Content>(generating: Content.Type, options: GenerationOptions, includeSchemaInPrompt: Bool, isolation: isolated (any Actor)?, prompt: () throws -> Prompt) async throws -> sending LanguageModelSession.Response<Content>](languagemodelsession/respond(generating:options:includeschemainprompt:isolation:prompt:).md)
  Produces a generable object as a response to a prompt.
- [func respond(options: GenerationOptions, isolation: isolated (any Actor)?, prompt: () throws -> Prompt) async throws -> sending LanguageModelSession.Response<String>](languagemodelsession/respond(options:isolation:prompt:).md)
  Produces a response to a prompt.
- [func respond(options: GenerationOptions, schema: GenerationSchema, includeSchemaInPrompt: Bool, isolation: isolated (any Actor)?, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](languagemodelsession/respond(options:schema:includeschemainprompt:isolation:prompt:).md)
  Produces a generated content type as a response to a prompt and schema.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(to:generating:includeschemainprompt:options:isolation:))*