# respond(to:schema:options:contextOptions:metadata:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a generated content type as a response to a prompt and schema.

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
nonisolated(nonsending) final func respond(to prompt: String, schema: GenerationSchema, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(includeSchemaInPrompt: true), metadata: [String : any ConvertibleToGeneratedContent] = [:]) async throws -> LanguageModelSession.Response<GeneratedContent>
```

**Other overloads**:

```swift
@discardableResult
nonisolated(nonsending) final func respond(to prompt: Prompt, schema: GenerationSchema, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(includeSchemaInPrompt: true), metadata: [String : any ConvertibleToGeneratedContent] = [:]) async throws -> LanguageModelSession.Response<GeneratedContent>
```

## Return Value

[`GeneratedContent`](../generatedcontent.md) containing the fields and values defined in the schema.

## Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `schema`: A schema to guide the output with.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(to:schema:options:contextoptions:metadata:)-fi30)*