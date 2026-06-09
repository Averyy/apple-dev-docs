# respond(options:prompt:)

**Framework**: Foundation Models  
**Kind**: method

Produces a response to a prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
nonisolated(nonsending) final func respond(options: GenerationOptions = GenerationOptions(), @PromptBuilder prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>
```

#### Return Value

A string composed of the tokens produced by sampling model output.

## Parameters

- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `prompt`: A prompt for the model to respond to.

## See Also

- [var isResponding: Bool](languagemodelsession/isresponding.md)
  A Boolean value that indicates a response is being generated.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(options:prompt:))*