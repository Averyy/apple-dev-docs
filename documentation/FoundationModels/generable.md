# Generable

**Framework**: Foundation Models  
**Kind**: protocol

A type that the model uses when responding to prompts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol Generable : ConvertibleFromGeneratedContent, ConvertibleToGeneratedContent
```

## Mentions

- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)
- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

Annotate your Swift structure or enumeration with the `Generable` macro to allow the model to respond to prompts by generating an instance of your type. Use the `Guide` macro to provide natural language descriptions of your properties, and programmatically control the values that the model can generate.

```swift
@Generable
struct SearchSuggestions {
    @Guide(description: "A list of suggested search terms.", .count(4))
    var searchTerms: [SearchTerm]
    @Generable
    struct SearchTerm {
        // Use a generation identifier for data structures the framework generates.
        var id: GenerationID
        @Guide(description: "A two- or three- word search term, like 'Beautiful sunsets'.")
        var searchTerm: String
    }
}
```

For every [`Generable`](generable.md) type in a request, the framework converts its type and format information to a JSON schema and provides it to the model. This contributes to the available context window size. If the [`LanguageModelSession`](languagemodelsession.md) exceeds the available context size, it throws [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md). To reduce the size of your generable type:

- Reduce the complexity of your [`Generable`](generable.md) type by evaluating whether properties are necessary to complete the task.
- Give your properties short and clear names.
- Use [`Guide(description:)`](guide(description:).md) on properties only when it improves response quality.
- Add a [`Guide(description:_:)`](guide(description:_:).md) with [`maximumCount(_:)`](generationguide/maximumcount(_:).md) to reduce token usage.

If the [`Generable`](generable.md) type includes properties with clear names the model may have all it needs to generate your type, eliminating the need of [`Guide(description:)`](guide(description:).md). For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

## Topics

### Defining a generable type
- [macro Generable(description: String?)](generable(description:).md)
  Conforms a type to [`Generable`](generable.md) protocol.
### Creating a guide
- [macro Guide(description: String)](guide(description:).md)
  Allows for influencing the allowed values of properties of a [`Generable`](generable.md) type.
- [macro Guide(description:_:)](guide(description:_:).md)
  Allows for influencing the allowed values of properties of a [`Generable`](generable.md) type.
- [struct GenerationGuide](generationguide.md)
  Guides that control how values are generated.
### Getting the schema
- [static var generationSchema: GenerationSchema](generable/generationschema.md)
  An instance of the generation schema.
- [struct GenerationSchema](generationschema.md)
  A type that describes the properties of an object and any guides on their values.
### Generating a unique identifier
- [struct GenerationID](generationid.md)
  A unique identifier that is stable for the duration of a response, but not across responses.
### Converting to partially generated
- [func asPartiallyGenerated() -> Self.PartiallyGenerated](generable/aspartiallygenerated.md)
  The partially generated type of this struct.
- [associatedtype PartiallyGenerated : ConvertibleFromGeneratedContent = Self](generable/partiallygenerated.md)
  A representation of partially generated content
### Generate dynamic shemas
- [struct DynamicGenerationSchema](dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.

## Relationships

### Inherits From
- [ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
- [InstructionsRepresentable](instructionsrepresentable.md)
- [PromptRepresentable](promptrepresentable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [GeneratedContent](generatedcontent.md)

## See Also

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable)*