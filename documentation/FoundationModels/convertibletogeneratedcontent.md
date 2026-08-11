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
- watchOS 27.0+ (Beta)

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
- [ImageReference](imagereference.md)

## See Also

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [macro Generable(description: String?)](generable(description:).md)
- [macro Guide(description: String)](guide(description:).md)
- [protocol Generable](generable.md)
  A type that the model uses when responding to prompts.
- [struct GenerationSchema](generationschema.md)
  A type that describes the properties of an object and any guides on their values.
- [struct DynamicGenerationSchema](dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/convertibletogeneratedcontent)*