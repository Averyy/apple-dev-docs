# LanguageModelSession.ResponseStream

**Framework**: Foundation Models  
**Kind**: struct

A structure that  stores the output of a response stream.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ResponseStream<Content> where Content : Generable
```

## Topics

### Collecting the response stream
- [func collect(isolation: isolated (any Actor)?) async throws -> sending LanguageModelSession.Response<Content>](languagemodelsession/responsestream/collect(isolation:).md)
  The result from a streaming response, after it completes.
### Default Implementations
- [AsyncSequence Implementations](languagemodelsession/responsestream/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [func streamResponse(to:options:)](languagemodelsession/streamresponse(to:options:).md)
  Produces a response stream to a prompt.
- [func streamResponse(to:generating:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:generating:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(to:schema:includeSchemaInPrompt:options:)](languagemodelsession/streamresponse(to:schema:includeschemainprompt:options:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse<Content>(generating: Content.Type, options: GenerationOptions, includeSchemaInPrompt: Bool, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:options:includeschemainprompt:prompt:).md)
  Produces a response stream for a type.
- [func streamResponse(options: GenerationOptions, schema: GenerationSchema, includeSchemaInPrompt: Bool, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(options:schema:includeschemainprompt:prompt:).md)
  Produces a response stream to a prompt and schema.
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream)*