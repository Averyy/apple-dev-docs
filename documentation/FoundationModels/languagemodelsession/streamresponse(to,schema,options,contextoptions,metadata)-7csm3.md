# streamResponse(to:schema:options:contextOptions:metadata:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a response stream to a prompt and schema.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final func streamResponse(to prompt: String, schema: GenerationSchema, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(includeSchemaInPrompt: true), metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> sending LanguageModelSession.ResponseStream<GeneratedContent>
```

**Other overloads**:

```swift
final func streamResponse(to prompt: Prompt, schema: GenerationSchema, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(includeSchemaInPrompt: true), metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> sending LanguageModelSession.ResponseStream<GeneratedContent>
```

## Return Value

A response stream that produces [`GeneratedContent`](../generatedcontent.md) containing the fields and values defined in the schema.

## Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](./respond%28to,options%29-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelError.rateLimited(_:)`](../languagemodelerror/ratelimited%28_%29.md) errors.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `schema`: A schema to guide the output with.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(to:schema:options:contextoptions:metadata:)-7csm3)*