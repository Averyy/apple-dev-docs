# ConvertibleFromGeneratedContent

**Framework**: Foundation Models  
**Kind**: protocol

A type that can be initialized from generated content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol ConvertibleFromGeneratedContent
```

## Topics

### Creating a convertable
- [init(GeneratedContent) throws](convertiblefromgeneratedcontent/init(_:).md)
  Creates an instance with the content.

## Relationships

### Inherited By
- [Generable](generable.md)
### Conforming Types
- [GeneratedContent](generatedcontent.md)

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
- [LanguageModelSession.ResponseStream](languagemodelsession/responsestream.md)
  A structure that  stores the output of a response stream.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/convertiblefromgeneratedcontent)*