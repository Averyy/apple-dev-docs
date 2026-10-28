# respond(schema:includeSchemaInPrompt:options:prompt:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a generated content type as a response to a prompt and schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
nonisolated(nonsending) final func respond(schema: GenerationSchema, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions(), @PromptBuilder prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>
```

## Return Value

[`GeneratedContent`](../generatedcontent.md) containing the fields and values defined in the schema.

## Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

## Parameters

- `schema`: A schema to guide the output with.
- `includeSchemaInPrompt`: If `true`, injects the schema into the prompt to bias the model.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `prompt`: A prompt for the model to respond to.

## See Also

### Generating a response
- [var isResponding: Bool](./isresponding.md)
  A Boolean value that indicates whether a response is being generated.
- [func respond(options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>](./respond%28options,prompt%29.md)
  Produces a response to a prompt.
- [func respond<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<Content>](./respond%28generating,includeschemainprompt,options,prompt%29.md)
  Produces a generable object as a response to a prompt.
- [func respond(to:options:)](./respond%28to,options%29.md)
  Produces a response to a prompt.
- [func respond(to:generating:includeSchemaInPrompt:options:)](./respond%28to,generating,includeschemainprompt,options%29.md)
  Produces a generable object as a response to a prompt.
- [func respond(to:schema:includeSchemaInPrompt:options:)](./respond%28to,schema,includeschemainprompt,options%29.md)
  Produces a generated content type as a response to a prompt and schema.
- [LanguageModelSession.Response](./response.md)
  A structure that stores the output of a response call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(schema:includeschemainprompt:options:prompt:))*