# init(type:description:anyOf:)

**Framework**: Foundation Models  
**Kind**: init

Creates a schema for a string enumeration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(type: any Generable.Type, description: String? = nil, anyOf choices: [String])
```

## Parameters

- `type`: The type this schema represents.
- `description`: A natural language description of this schema.
- `choices`: The allowed choices.

## See Also

- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](generationschema/init(root:dependencies:).md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](generationschema/init(type:description:properties:).md)
  Creates a schema by providing an array of properties.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](generationschema/init(type:description:representnilexplicitlyingeneratedcontent:properties:).md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](generationschema/property.md)
  Fields are named members of object types. Fields are strongly typed and have optional descriptions and guides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/init(type:description:anyof:))*