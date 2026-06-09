# GeneratedContent

**Framework**: Foundation Models  
**Kind**: struct

A type that represents structured, generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct GeneratedContent
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

Generated content may contain a single value, an array, or key-value pairs with unique keys.

## Topics

### Creating generated content
- [init(_:)](generatedcontent/init(_:).md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](generatedcontent/init(_:id:).md)
  Creates content that contains a single value with a custom `GenerationID`.
- [init<S>(elements: S, id: GenerationID?)](generatedcontent/init(elements:id:).md)
  Creates content representing an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](generatedcontent/init(properties:id:).md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](generatedcontent/init(properties:id:uniquingkeyswith:).md)
  Creates new generated content from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init(json: String) throws](generatedcontent/init(json:).md)
  Creates equivalent content from a JSON string.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](generatedcontent/init(kind:id:).md)
  Creates a new `GeneratedContent` instance with the specified kind and `GenerationID`.
- [GeneratedContent.ParsingError](generatedcontent/parsingerror.md)
  A failure that occurs when a string cannot be parsed into GeneratedContent.
- [static let null: GeneratedContent](generatedcontent/null.md)
### Accessing the content
- [var kind: GeneratedContent.Kind](generatedcontent/kind-swift.property.md)
  The representation of the generated content.
- [GeneratedContent.Kind](generatedcontent/kind-swift.enum.md)
  A representation of the different types of content that can be stored in generated content.
- [func value<Value>(Value.Type) throws -> Value](generatedcontent/value(_:).md)
  Reads a top level, concrete partially `Generable` type from a named property.
- [func value(_:forProperty:)](generatedcontent/value(_:forproperty:).md)
  Reads a concrete `Generable` type from named property.
- [var isComplete: Bool](generatedcontent/iscomplete.md)
  A Boolean that indicates whether the generated content is completed.
- [var generatedContent: GeneratedContent](generatedcontent/generatedcontent.md)
  A representation of this instance.
- [var jsonString: String](generatedcontent/jsonstring.md)
  Returns a JSON string representation of the generated content.
- [var debugDescription: String](generatedcontent/debugdescription.md)
  A string representation for the debug description.
### Identifying a generation
- [var id: GenerationID?](generatedcontent/id.md)
  A unique id that is stable for the duration of a generated response.
- [struct GenerationID](generationid.md)
  A unique identifier that is stable for the duration of a response, but not across responses.

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

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [protocol Generable](generable.md)
  A type that the model uses when responding to prompts.
- [struct GenerationSchema](generationschema.md)
  A type that describes the properties of an object and any guides on their values.
- [struct DynamicGenerationSchema](dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent)*