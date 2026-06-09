# LanguageModelSession.ResponseStream

**Framework**: Foundation Models  
**Kind**: struct

An async sequence of snapshots of partially generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ResponseStream<Content> where Content : Generable
```

## Topics

### Collecting the response stream
- [func collect() async throws -> sending LanguageModelSession.Response<Content>](languagemodelsession/responsestream/collect.md)
  The result from a streaming response, after it completes.
### Getting a snapshot of a partial response
- [LanguageModelSession.ResponseStream.Snapshot](languagemodelsession/responsestream/snapshot.md)
  A snapshot of partially generated content.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)

## See Also

- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:includeschemainprompt:options:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:options:)](languagemodelsession/streamresponse(to:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:generating:includeschemainprompt:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:schema:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream)*