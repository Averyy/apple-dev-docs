# GenerationSchema

**Framework**: Foundation Models  
**Kind**: struct

A type that describes the properties of an object and any guides on their values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct GenerationSchema
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

Generation  schemas guide the output of a [`SystemLanguageModel`](systemlanguagemodel.md) to deterministically ensure the output is in the desired format.

## Topics

### Creating a generation schema
- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](generationschema/init(root:dependencies:).md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type:description:anyOf:)](generationschema/init(type:description:anyof:).md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](generationschema/init(type:description:properties:).md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](generationschema/property.md)
  A property that belongs to a generation schema.
### Getting the debug description
- [var debugDescription: String](generationschema/debugdescription.md)
  A string representation of the debug description.
### Getting the generation schema error types
- [GenerationSchema.SchemaError](generationschema/schemaerror.md)
  A error that occurs when there is a problem creating a generation schema.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var generationSchema: GenerationSchema](generable/generationschema.md)
  An instance of the generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema)*