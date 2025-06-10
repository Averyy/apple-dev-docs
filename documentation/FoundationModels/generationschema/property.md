# GenerationSchema.Property

**Framework**: Foundation Models  
**Kind**: struct

A property that belongs to a generation schema.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Property
```

#### Overview

Fields are named members of object types. Fields are strongly typed and have optional descriptions and guides.

## Topics

### Creating a property
- [init(name:description:type:guides:)](generationschema/property/init(name:description:type:guides:).md)
  Create a property that contains a string type.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/property)*