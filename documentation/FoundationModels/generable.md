# Generable

**Framework**: Foundation Models  
**Kind**: protocol

A type that the model uses when responding to prompts.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol Generable : ConvertibleFromGeneratedContent, ConvertibleToGeneratedContent
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

Annotate your Swift structure or enumeration with the `@Generable` macro to allow the model to respond to prompts by generating an instance of your type. Use the `@Guide` macro to provide natural language descriptions of your properties, and programmatically control the values that the model can generate.

```swift
@Generable
struct SearchSuggestions {
    @Guide(description: "A list of suggested search terms", .count(4))
    var searchTerms: [SearchTerm]

    @Generable
    struct SearchTerm {
        // Use a generation identifier for types the framework generates.
        var id: GenerationID

        @Guide(description: "A 2 or 3 word search term, like 'Beautiful sunsets'")
        var searchTerm: String
    }
}
```

## Topics

### Defining a generable type
- [macro Generable(description: String?)](generable(description:).md)
  Conforms a type to generable.
### Creating a guide
- [macro Guide(description: String)](guide(description:).md)
  Allows for influencing the allowed values of properties of a generable type.
- [macro Guide(description:_:)](guide(description:_:).md)
  Allows for influencing the allowed values of properties of a generable type.
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
### Conforming Types
- [GeneratedContent](generatedcontent.md)

## See Also

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable)*