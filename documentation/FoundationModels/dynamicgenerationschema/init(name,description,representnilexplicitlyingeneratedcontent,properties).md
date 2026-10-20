# init(name:description:representNilExplicitlyInGeneratedContent:properties:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an object schema.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- watchOS 27.0+

## Declaration

```swift
init(name: String, description: String? = nil, representNilExplicitlyInGeneratedContent explicitNil: Bool, properties: [DynamicGenerationSchema.Property])
```

## Parameters

- `name`: A name this dynamic schema can be referenced by.
- `description`: A natural language description of this schema.
- `properties`: The properties associated with this schema.

## See Also

### Creating a dynamic schema
- [init(arrayOf: DynamicGenerationSchema, minimumElements: Int?, maximumElements: Int?)](./init%28arrayof,minimumelements,maximumelements%29.md)
  Creates an array schema.
- [init(name:description:anyOf:)](./init%28name,description,anyof%29.md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](./init%28name,description,properties%29.md)
  Creates an object schema.
- [init(referenceTo: String)](./init%28referenceto%29.md)
  Creates a reference schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](./init%28type,guides%29.md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](./property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(name:description:representnilexplicitlyingeneratedcontent:properties:))*