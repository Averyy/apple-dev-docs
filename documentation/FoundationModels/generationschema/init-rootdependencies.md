# init(root:dependencies:)

**Framework**: Foundation Models  
**Kind**: init

Creates a schema by providing an array of dynamic schemas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws
```

#### Discussion

> **Note**: Throws there are schemas with naming conflicts or references to undefined types.

## Parameters

- `root`: The root schema.
- `dependencies`: An array of dynamic schemas.

## See Also

- [init(type:description:anyOf:)](generationschema/init(type:description:anyof:).md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](generationschema/init(type:description:properties:).md)
  Creates a schema by providing an array of properties.
- [GenerationSchema.Property](generationschema/property.md)
  A property that belongs to a generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/init(root:dependencies:))*