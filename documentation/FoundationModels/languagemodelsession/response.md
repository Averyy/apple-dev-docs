# LanguageModelSession.Response

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A structure that stores the output of a response call.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct Response<Content> where Content : Generable
```

## Topics

### Getting the response content
- [let content: Content](./response/content.md)
  The response content.
- [let rawContent: GeneratedContent](./response/rawcontent.md)
  The raw response content.
### Inspecting the usage tokens
- [let usage: LanguageModelSession.Usage](./response/usage.md)
  Information about how many tokens were used by this response.
### Getting the transcript entries
- [let transcriptEntries: ArraySlice<Transcript.Entry>](./response/transcriptentries.md)
  The list of transcript entries.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Generating a response
- [var isResponding: Bool](./isresponding.md)
  A Boolean value that indicates whether a response is being generated.
- [func respond(options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<String>](./respond%28options,prompt%29.md)
  Produces a response to a prompt.
- [func respond<Content>(generating: Content.Type, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<Content>](./respond%28generating,includeschemainprompt,options,prompt%29.md)
  Produces a generable object as a response to a prompt.
- [func respond(schema: GenerationSchema, includeSchemaInPrompt: Bool, options: GenerationOptions, prompt: () throws -> Prompt) async throws -> LanguageModelSession.Response<GeneratedContent>](./respond%28schema,includeschemainprompt,options,prompt%29.md)
  Produces a generated content type as a response to a prompt and schema.
- [func respond(to:options:)](./respond%28to,options%29.md)
  Produces a response to a prompt.
- [func respond(to:generating:includeSchemaInPrompt:options:)](./respond%28to,generating,includeschemainprompt,options%29.md)
  Produces a generable object as a response to a prompt.
- [func respond(to:schema:includeSchemaInPrompt:options:)](./respond%28to,schema,includeschemainprompt,options%29.md)
  Produces a generated content type as a response to a prompt and schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/response)*