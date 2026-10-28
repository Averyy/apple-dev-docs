# GeneratedContent

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that represents structured, generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct GeneratedContent
```

## Mentions

- [Expanding generation with tool calling](./expanding-generation-with-tool-calling.md)
- [Generating Swift data structures with guided generation](./generating-swift-data-structures-with-guided-generation.md)

## Overview

Generated content may contain a single value, an array, or key-value pairs with unique keys.

## Topics

### Creating generated content
- [init(_:)](./generatedcontent/init%28_%29.md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](./generatedcontent/init%28_,id%29.md)
  Creates content that contains a single value with a custom generation identifier.
- [init<S>(elements: S, id: GenerationID?)](./generatedcontent/init%28elements,id%29.md)
  Creates content representing an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](./generatedcontent/init%28properties,id%29.md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](./generatedcontent/init%28properties,id,uniquingkeyswith%29.md)
  Creates generated content from key-value pairs, resolving duplicate keys with a combining closure.
- [init(json: String) throws](./generatedcontent/init%28json%29.md)
  Creates equivalent content from a JSON string.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](./generatedcontent/init%28kind,id%29.md)
  Creates content with the specified kind and generation identifier.
- [GeneratedContent.ParsingError](./generatedcontent/parsingerror.md)
  A failure that occurs when a string cannot be parsed into generated content.
### Accessing the content
- [var kind: GeneratedContent.Kind](./generatedcontent/kind-swift.property.md)
  The representation of the generated content.
- [GeneratedContent.Kind](./generatedcontent/kind-swift.enum.md)
  A representation of the different types of content that can be stored in generated content.
- [func value<Value>(Value.Type) throws -> Value](./generatedcontent/value%28_%29.md)
  Reads a top level, concrete partially generable type from a named property.
- [func value(_:forProperty:)](./generatedcontent/value%28_,forproperty%29.md)
  Reads a concrete generable type from a named property.
- [var isComplete: Bool](./generatedcontent/iscomplete.md)
  A Boolean value that indicates whether the generated content is complete.
- [var generatedContent: GeneratedContent](./generatedcontent/generatedcontent.md)
  A representation of this instance.
- [var jsonString: String](./generatedcontent/jsonstring.md)
  A JSON string representation of the generated content.
- [var debugDescription: String](./generatedcontent/debugdescription.md)
  A string representation for the debug description.
### Identifying a generation
- [var id: GenerationID?](./generatedcontent/id.md)
  A unique id that is stable for the duration of a generated response.
- [struct GenerationID](./generationid.md)
  A unique identifier that is stable for the duration of a response, but not across responses.
### Default Implementations
- [ConvertibleFromGeneratedContent Implementations](./generatedcontent/convertiblefromgeneratedcontent-implementations.md)
- [ConvertibleToGeneratedContent Implementations](./generatedcontent/convertibletogeneratedcontent-implementations.md)
- [CustomDebugStringConvertible Implementations](./generatedcontent/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](./convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](./convertibletogeneratedcontent.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Generable](./generable.md)
- [InstructionsRepresentable](./instructionsrepresentable.md)
- [PromptRepresentable](./promptrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Structured output
- [Generating Swift data structures with guided generation](./generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [macro Generable(description: String?)](./generable%28description%29.md)
- [macro Guide(description: String)](./guide%28description%29.md)
- [protocol Generable](./generable.md)
  A type that the model uses when responding to prompts.
- [struct GenerationSchema](./generationschema.md)
  A type that describes the properties of an object and any guides on their values.
- [struct DynamicGenerationSchema](./dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [protocol ConvertibleToGeneratedContent](./convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](./convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent)*