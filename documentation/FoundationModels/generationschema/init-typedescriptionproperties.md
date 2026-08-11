# init(type:description:properties:)

**Framework**: Foundation Models  
**Kind**: init

Creates a schema by providing an array of properties.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(type: any Generable.Type, description: String? = nil, properties: [GenerationSchema.Property])
```

## Parameters

- `type`: The type this schema represents.
- `description`: A natural language description of this schema.
- `properties`: An array of properties.

## See Also

- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](generationschema/init(root:dependencies:).md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type:description:anyOf:)](generationschema/init(type:description:anyof:).md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](generationschema/init(type:description:representnilexplicitlyingeneratedcontent:properties:).md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](generationschema/property.md)
  A named, strongly typed member of an object type with an optional description and guides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/init(type:description:properties:))*