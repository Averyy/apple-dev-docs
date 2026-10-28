# streamResponse(to:generating:includeSchemaInPrompt:options:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a response stream to a prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
final func streamResponse<Content>(to prompt: String, generating type: Content.Type = Content.self, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions()) -> sending LanguageModelSession.ResponseStream<Content> where Content : Generable
```

**Other overloads**:

```swift
final func streamResponse<Content>(to prompt: Prompt, generating type: Content.Type = Content.self, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions()) -> sending LanguageModelSession.ResponseStream<Content> where Content : Generable
```

## Return Value

A response stream that produces [`GeneratedContent`](../generatedcontent.md) containing the fields and values defined in the schema.

## Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](./respond%28to,options%29-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelError.rateLimited(_:)`](../languagemodelerror/ratelimited%28_%29.md) errors.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `type`: A type to produce as the response.
- `includeSchemaInPrompt`: If `true`, injects the schema into the prompt to bias the model.
- `options`: Options that control how tokens are sampled from the distribution the model produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(to:generating:includeschemainprompt:options:)-8x6iv)*