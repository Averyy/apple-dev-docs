# init(referenceTo:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a reference schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(referenceTo name: String)
```

## Parameters

- `name`: The name of the [`DynamicGenerationSchema`](../dynamicgenerationschema.md) this is a reference to.

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
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](./init%28type,guides%29.md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](./property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(referenceto:))*