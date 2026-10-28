# init(root:dependencies:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a schema by providing an array of dynamic schemas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws
```

## Discussion

> **Throws**: If there are schemas with naming conflicts or references to undefined types.

## Parameters

- `root`: The root schema.
- `dependencies`: An array of dynamic schemas.

## See Also

### Creating a generation schema
- [init(type:description:anyOf:)](./init%28type,description,anyof%29.md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](./init%28type,description,properties%29.md)
  Creates a schema by providing an array of properties.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](./init%28type,description,representnilexplicitlyingeneratedcontent,properties%29.md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](./property.md)
  A named, strongly typed member of an object type with an optional description and guides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/init(root:dependencies:))*