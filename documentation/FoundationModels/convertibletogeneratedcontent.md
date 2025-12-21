# ConvertibleToGeneratedContent

**Framework**: Foundation Models  
**Kind**: protocol

A type that can be converted to generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol ConvertibleToGeneratedContent : InstructionsRepresentable, PromptRepresentable
```

## Topics

### Getting the generated content
- [var generatedContent: GeneratedContent](convertibletogeneratedcontent/generatedcontent.md)
  This instance represented as generated content.

## Relationships

### Inherits From
- [InstructionsRepresentable](instructionsrepresentable.md)
- [PromptRepresentable](promptrepresentable.md)
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
- [func streamResponse(options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<String>](languagemodelsession/streamresponse(options:prompt:).md)
  Produces a response stream to a prompt.
- [func streamResponse<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<Content>](languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:).md)
  Produces a response stream for a type.
- [func streamResponse(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) rethrows -> sending LanguageModelSession.ResponseStream<GeneratedContent>](languagemodelsession/streamresponse(schema:includeschemainprompt:options:prompt:).md)
  Produces a response stream to a prompt and schema.
- [LanguageModelSession.ResponseStream](languagemodelsession/responsestream.md)
  An async sequence of snapshots of partially generated content.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/convertibletogeneratedcontent)*