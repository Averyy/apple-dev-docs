# GenerationSchema

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that describes the properties of an object and any guides on their values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct GenerationSchema
```

## Mentions

- [Generating Swift data structures with guided generation](./generating-swift-data-structures-with-guided-generation.md)

#### Overview

Generation schemas guide the output of a language model to deterministically ensure the output is in the desired format.

## Topics

### Creating a generation schema
- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](./generationschema/init%28root,dependencies%29.md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type:description:anyOf:)](./generationschema/init%28type,description,anyof%29.md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](./generationschema/init%28type,description,properties%29.md)
  Creates a schema by providing an array of properties.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](./generationschema/init%28type,description,representnilexplicitlyingeneratedcontent,properties%29.md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](./generationschema/property.md)
  A named, strongly typed member of an object type with an optional description and guides.
### Accessing the name
- [var name: String](./generationschema/name.md)
  The name of this generation schema.
### Errors
- [GenerationSchema.SchemaError](./generationschema/schemaerror.md)
  An error that occurs when there is a problem creating a generation schema.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
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
- [struct DynamicGenerationSchema](./dynamicgenerationschema.md)
  The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.
- [struct GeneratedContent](./generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleToGeneratedContent](./convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](./convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema)*