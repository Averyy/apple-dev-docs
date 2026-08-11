# Generable(description:)

**Framework**: Foundation Models  
**Kind**: macro

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@attached
(extension, conformances: Generable, names: named(init(_:)), named(generatedContent)) @attached(member, names: arbitrary) macro Generable(description: String? = nil)
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

## See Also

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [macro Guide(description: String)](guide(description:).md)
- [protocol Generable](generable.md)
  A type that the model uses when responding to prompts.
- [struct GenerationSchema](generationschema.md)
  A type that describes the properties of an object and any guides on their values.
- [struct DynamicGenerationSchema](dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(description:))*