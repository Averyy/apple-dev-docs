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
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct GenerationSchema
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

Generation schemas guide the output of a language model to deterministically ensure the output is in the desired format.

## Topics

### Creating a generation schema
- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](generationschema/init(root:dependencies:).md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type:description:anyOf:)](generationschema/init(type:description:anyof:).md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](generationschema/init(type:description:properties:).md)
  Creates a schema by providing an array of properties.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](generationschema/init(type:description:representnilexplicitlyingeneratedcontent:properties:).md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](generationschema/property.md)
  Fields are named members of object types. Fields are strongly typed and have optional descriptions and guides.
### Accessing the name
- [var name: String](generationschema/name.md)
  The name of this generation schema.
### Errors
- [GenerationSchema.SchemaError](generationschema/schemaerror.md)
  A error that occurs when there is a problem creating a generation schema.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)
  Create robust apps by describing output you want programmatically.
- [protocol Generable](generable.md)
  A type that the model uses when responding to prompts.
- [struct DynamicGenerationSchema](dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [struct GeneratedContent](generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema)*