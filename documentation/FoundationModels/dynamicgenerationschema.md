# DynamicGenerationSchema

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct DynamicGenerationSchema
```

## Mentions

- [Generating Swift data structures with guided generation](./generating-swift-data-structures-with-guided-generation.md)

## Overview

An individual schema may reference other schemas by name, and references are resolved when converting a set of dynamic schemas into a [`GenerationSchema`](./generationschema.md).

## Topics

### Creating a dynamic schema
- [init(arrayOf: DynamicGenerationSchema, minimumElements: Int?, maximumElements: Int?)](./dynamicgenerationschema/init%28arrayof,minimumelements,maximumelements%29.md)
  Creates an array schema.
- [init(name:description:anyOf:)](./dynamicgenerationschema/init%28name,description,anyof%29.md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](./dynamicgenerationschema/init%28name,description,properties%29.md)
  Creates an object schema.
- [init(name: String, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [DynamicGenerationSchema.Property])](./dynamicgenerationschema/init%28name,description,representnilexplicitlyingeneratedcontent,properties%29.md)
  Creates an object schema.
- [init(referenceTo: String)](./dynamicgenerationschema/init%28referenceto%29.md)
  Creates a reference schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](./dynamicgenerationschema/init%28type,guides%29.md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](./dynamicgenerationschema/property.md)
  A property that belongs to a dynamic generation schema.
### Creating a null schema
- [static var null: DynamicGenerationSchema](./dynamicgenerationschema/null.md)
  A schema that represents a null value.

## Relationships

### Conforms To
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
- [struct GeneratedContent](./generatedcontent.md)
  A type that represents structured, generated content.
- [protocol ConvertibleToGeneratedContent](./convertibletogeneratedcontent.md)
  A type that can be converted to generated content.
- [protocol ConvertibleFromGeneratedContent](./convertiblefromgeneratedcontent.md)
  A type that can be initialized from generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema)*