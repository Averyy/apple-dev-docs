# streamResponse(to:options:contextOptions:metadata:)

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
final func streamResponse(to prompt: Prompt, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(), metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> sending LanguageModelSession.ResponseStream<String>
```

#### Return Value

A response stream that produces aggregated tokens.

#### Discussion

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelError.rateLimited(_:)`](languagemodelerror/ratelimited(_:).md) errors.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.

## See Also

- [func streamResponse(options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:options:contextoptions:metadata:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:generating:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:generating:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:options:contextOptions:metadata:)](languagemodelsession/streamresponse(to:schema:options:contextoptions:metadata:).md)
  Produces a response stream to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(to:options:contextoptions:metadata:))*