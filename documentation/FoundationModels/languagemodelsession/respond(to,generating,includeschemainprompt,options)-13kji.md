# respond(to:generating:includeSchemaInPrompt:options:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a generable object as a response to a prompt.

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
nonisolated(nonsending) final func respond<Content>(to prompt: String, generating type: Content.Type = Content.self, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions()) async throws -> LanguageModelSession.Response<Content> where Content : Generable
```

**Other overloads**:

```swift
@discardableResult
nonisolated(nonsending) final func respond<Content>(to prompt: Prompt, generating type: Content.Type = Content.self, includeSchemaInPrompt: Bool = true, options: GenerationOptions = GenerationOptions()) async throws -> LanguageModelSession.Response<Content> where Content : Generable
```

## Mentions

- [Generating Swift data structures with guided generation](../generating-swift-data-structures-with-guided-generation.md)

## Return Value

[`GeneratedContent`](../generatedcontent.md) containing the fields and values defined in the schema.

## Discussion

Consider using the default value of `true` for `includeSchemaInPrompt`. The exception to the rule is when the model has knowledge about the expected response format, either because it has been trained on it, or because it has seen exhaustive examples during this session.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `type`: A type to produce as the response.
- `includeSchemaInPrompt`: If `true`, injects the schema into the prompt to bias the model.
- `options`: Options that control how tokens are sampled from the distribution the model produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(to:generating:includeschemainprompt:options:)-13kji)*