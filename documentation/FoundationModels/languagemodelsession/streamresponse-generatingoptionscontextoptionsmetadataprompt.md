# streamResponse(generating:options:contextOptions:metadata:prompt:)

**Framework**: Foundation Models  
**Kind**: method

Produces a response stream to a prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final func streamResponse<Content>(generating type: Content.Type = Content.self, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(includeSchemaInPrompt: true), metadata: [String : any Sendable & Codable & Equatable] = [:], @PromptBuilder prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content> where Content : Generable
```

#### Return Value

A response stream that produces [`GeneratedContent`](generatedcontent.md) containing the fields and values defined in the schema.

#### Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelError.rateLimited(_:)`](languagemodelerror/ratelimited(_:).md) errors.

## Parameters

- `type`: A type to produce as the response.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.
- `prompt`: A prompt for the model to respond to.

## See Also

- [func streamResponse(options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any Sendable & Codable & Equatable], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any Sendable & Codable & Equatable], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:generating:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:schema:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(generating:options:contextoptions:metadata:prompt:))*