# streamResponse(options:contextOptions:metadata:prompt:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a response stream to a prompt.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final func streamResponse(options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(), metadata: [String : any ConvertibleToGeneratedContent] = [:], @PromptBuilder prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>
```

## Return Value

A response stream that produces aggregated tokens.

## Discussion

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](./respond%28to,options%29-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelError.rateLimited(_:)`](../languagemodelerror/ratelimited%28_%29.md) errors.

## Parameters

- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.
- `prompt`: A prompt for the model to respond to.

## See Also

### Streaming a response with metadata
- [func streamResponse<Content>(generating: Content.Type, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](./streamresponse%28generating,options,contextoptions,metadata,prompt%29.md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](./streamresponse%28schema,options,contextoptions,metadata,prompt%29.md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:options:contextOptions:metadata:)](./streamresponse%28to,options,contextoptions,metadata%29.md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:options:contextOptions:metadata:)](./streamresponse%28to,generating,options,contextoptions,metadata%29.md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:options:contextOptions:metadata:)](./streamresponse%28to,schema,options,contextoptions,metadata%29.md)
  Produces a response stream to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(options:contextoptions:metadata:prompt:))*