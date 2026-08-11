# GenerationSchema.Property

**Framework**: Foundation Models  
**Kind**: struct

A named, strongly typed member of an object type with an optional description and guides.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Property
```

## Topics

### Creating a property
- [init(name:description:type:guides:)](generationschema/property/init(name:description:type:guides:).md)
  Creates a property that contains a string type.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](generationschema/init(root:dependencies:).md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type:description:anyOf:)](generationschema/init(type:description:anyof:).md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](generationschema/init(type:description:properties:).md)
  Creates a schema by providing an array of properties.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](generationschema/init(type:description:representnilexplicitlyingeneratedcontent:properties:).md)
  Creates a schema by providing an array of properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/property)*