# GeneratedContent

**Framework**: Foundation Models  
**Kind**: struct

A type that represents structured, generated content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct GeneratedContent
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Overview

Generated content may contain a single value, an ordered collection of properties, or an ordered collection of values.

## Topics

### Creating generated values
- [init(_:)](generatedcontent/init(_:).md)
  Creates an object with the content you specify.
- [init<C>(elements: C)](generatedcontent/init(elements:).md)
  Creates an object with an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>)](generatedcontent/init(properties:).md)
  Creates an object with the properties you specify.
### Accessing the properties
- [func properties() throws -> [String : GeneratedContent]](generatedcontent/properties.md)
  Reads the properties of a top level object
### Getting the debug description
- [var debugDescription: String](generatedcontent/debugdescription.md)
  A string representation for the debug description.
### Reads a value from the concrete type
- [func value<Value>(Value.Type) throws -> Value](generatedcontent/value(_:).md)
  Reads a top level, concrete partially generable type.
- [func value(_:forProperty:)](generatedcontent/value(_:forproperty:).md)
  Reads a concrete generable type from named property.
### Retrieving the schema and content
- [static var generationSchema: GenerationSchema](generatedcontent/generationschema.md)
  An instance of the generation schema.
- [var generatedContent: GeneratedContent](generatedcontent/generatedcontent.md)
  A representation of this instance.
- [GeneratedContent.PartiallyGenerated](generatedcontent/partiallygenerated.md)
  A representation of partially generated content
### Getting the elements and generated content
- [func elements() throws -> [GeneratedContent]](generatedcontent/elements.md)
  Reads a top level array of content.
### Comparing generated content
- [static func == (GeneratedContent, GeneratedContent) -> Bool](generatedcontent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Getting the unique generation id
- [var id: GenerationID?](generatedcontent/id.md)
  A unique ID used for the duration of a generated response.
### Default Implementations
- [Equatable Implementations](generatedcontent/equatable-implementations.md)
- [Generable Implementations](generatedcontent/generable-implementations.md)
- [InstructionsRepresentable Implementations](generatedcontent/instructionsrepresentable-implementations.md)
- [PromptRepresentable Implementations](generatedcontent/promptrepresentable-implementations.md)

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Generable](generable.md)
- [InstructionsRepresentable](instructionsrepresentable.md)
- [PromptRepresentable](promptrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent)*