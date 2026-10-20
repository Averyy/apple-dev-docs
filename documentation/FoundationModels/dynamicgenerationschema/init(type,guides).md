# init(type:guides:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a schema from a generable type and guides.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init<Value>(type: Value.Type, guides: [GenerationGuide<Value>] = []) where Value : Generable
```

## Parameters

- `type`: A `Generable` type
- `guides`: Generation guides to apply to this `DynamicGenerationSchema`.

## See Also

### Creating a dynamic schema
- [init(arrayOf: DynamicGenerationSchema, minimumElements: Int?, maximumElements: Int?)](./init%28arrayof,minimumelements,maximumelements%29.md)
  Creates an array schema.
- [init(name:description:anyOf:)](./init%28name,description,anyof%29.md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](./init%28name,description,properties%29.md)
  Creates an object schema.
- [init(name: String, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [DynamicGenerationSchema.Property])](./init%28name,description,representnilexplicitlyingeneratedcontent,properties%29.md)
  Creates an object schema.
- [init(referenceTo: String)](./init%28referenceto%29.md)
  Creates a reference schema.
- [DynamicGenerationSchema.Property](./property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(type:guides:))*