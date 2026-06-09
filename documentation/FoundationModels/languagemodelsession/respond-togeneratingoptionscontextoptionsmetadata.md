# respond(to:generating:options:contextOptions:metadata:)

**Framework**: Foundation Models  
**Kind**: method

Produces a generable object as a response to a prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
nonisolated(nonsending) final func respond<Content>(to prompt: Prompt, generating type: Content.Type = Content.self, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(includeSchemaInPrompt: true), metadata: [String : any Sendable & Codable & Equatable] = [:]) async throws -> LanguageModelSession.Response<Content> where Content : Generable
```

#### Return Value

[`GeneratedContent`](generatedcontent.md) containing the fields and values defined in the schema.

#### Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `type`: A type to produce as the response.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.

## See Also

- [func respond(options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any Sendable & Codable & Equatable], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>](languagemodelsession/respond(options:contextoptions:metadata:prompt:).md)
  Produces a response to a prompt.
- [func respond<Content>(generating: Content.Type, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any Sendable & Codable & Equatable], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<Content>](languagemodelsession/respond(generating:options:contextoptions:metadata:prompt:).md)
  Produces a generable object as a response to a prompt.
- [func respond(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any Sendable & Codable & Equatable], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](languagemodelsession/respond(schema:options:contextoptions:metadata:prompt:).md)
  Produces a generated content type as a response to a prompt and schema.
- [func respond(to:options:contextOptions:metadata:)](languagemodelsession/respond(to:options:contextoptions:metadata:).md)
  Produces a response to a prompt.
- [func respond(to:schema:options:contextOptions:metadata:)](languagemodelsession/respond(to:schema:options:contextoptions:metadata:).md)
  Produces a generated content type as a response to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(to:generating:options:contextoptions:metadata:))*