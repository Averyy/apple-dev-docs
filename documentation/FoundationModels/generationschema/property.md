# GenerationSchema.Property

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A named, strongly typed member of an object type with an optional description and guides.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct Property
```

## Topics

### Creating a property
- [init(name:description:type:guides:)](./property/init%28name,description,type,guides%29.md)
  Creates a property that contains a string type.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a generation schema
- [init(root: DynamicGenerationSchema, dependencies: [DynamicGenerationSchema]) throws](./init%28root,dependencies%29.md)
  Creates a schema by providing an array of dynamic schemas.
- [init(type:description:anyOf:)](./init%28type,description,anyof%29.md)
  Creates a schema for a string enumeration.
- [init(type: any Generable.Type, description: String?, properties: [GenerationSchema.Property])](./init%28type,description,properties%29.md)
  Creates a schema by providing an array of properties.
- [init(type: any Generable.Type, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [GenerationSchema.Property])](./init%28type,description,representnilexplicitlyingeneratedcontent,properties%29.md)
  Creates a schema by providing an array of properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/property)*