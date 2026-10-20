# LanguageModelSession.ResponseStream

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An async sequence of snapshots of partially generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct ResponseStream<Content> where Content : Generable
```

## Topics

### Collecting the response stream
- [func collect() async throws -> sending LanguageModelSession.Response<Content>](./responsestream/collect%28%29.md)
  Returns the result from a streaming response, after it completes.
### Getting a snapshot of a partial response
- [LanguageModelSession.ResponseStream.Snapshot](./responsestream/snapshot.md)
  A snapshot of partially generated content.
### Default Implementations
- [AsyncSequence Implementations](./responsestream/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Streaming a response
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](./streamresponse%28options,prompt%29.md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](./streamresponse%28generating,includeschemainprompt,options,prompt%29.md)
  Produces a response stream to a prompt.
- [func streamResponse(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](./streamresponse%28schema,includeschemainprompt,options,prompt%29.md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:options:)](./streamresponse%28to,options%29.md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:includeSchemaInPrompt:options:)](./streamresponse%28to,generating,includeschemainprompt,options%29.md)
  Produces a response stream to a prompt.
- [func streamResponse(to:schema:includeSchemaInPrompt:options:)](./streamresponse%28to,schema,includeschemainprompt,options%29.md)
  Produces a response stream to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream)*