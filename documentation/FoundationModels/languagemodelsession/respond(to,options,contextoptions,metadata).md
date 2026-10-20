# respond(to:options:contextOptions:metadata:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a response to a prompt.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
nonisolated(nonsending) final func respond(to prompt: Prompt, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(), metadata: [String : any ConvertibleToGeneratedContent] = [:]) async throws -> LanguageModelSession.Response<String>
```

**Other overloads**:

```swift
@discardableResult
nonisolated(nonsending) final func respond(to prompt: String, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(), metadata: [String : any ConvertibleToGeneratedContent] = [:]) async throws -> LanguageModelSession.Response<String>
```

#### Return Value

A string composed of the tokens produced by sampling model output.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.

## See Also

### Generating a response with metadata
- [func respond(options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>](./respond%28options,contextoptions,metadata,prompt%29.md)
  Produces a response to a prompt.
- [func respond<Content>(generating: Content.Type, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<Content>](./respond%28generating,options,contextoptions,metadata,prompt%29.md)
  Produces a generable object as a response to a prompt.
- [func respond(schema: GenerationSchema, options: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any ConvertibleToGeneratedContent], prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](./respond%28schema,options,contextoptions,metadata,prompt%29.md)
  Produces a generated content type as a response to a prompt and schema.
- [func respond(to:generating:options:contextOptions:metadata:)](./respond%28to,generating,options,contextoptions,metadata%29.md)
  Produces a generable object as a response to a prompt.
- [func respond(to:schema:options:contextOptions:metadata:)](./respond%28to,schema,options,contextoptions,metadata%29.md)
  Produces a generated content type as a response to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(to:options:contextoptions:metadata:))*