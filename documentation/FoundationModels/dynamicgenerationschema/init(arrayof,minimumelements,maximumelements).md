# init(arrayOf:minimumElements:maximumElements:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an array schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(arrayOf itemSchema: DynamicGenerationSchema, minimumElements: Int? = nil, maximumElements: Int? = nil)
```

## Parameters

- `itemSchema`: A schema to use as the elements of the array.
- `minimumElements`: A minimum number of elements the array should contain.
- `maximumElements`: The maximum number of element the array should contain.

## See Also

### Creating a dynamic schema
- [init(name:description:anyOf:)](./init%28name,description,anyof%29.md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](./init%28name,description,properties%29.md)
  Creates an object schema.
- [init(name: String, description: String?, representNilExplicitlyInGeneratedContent: Bool, properties: [DynamicGenerationSchema.Property])](./init%28name,description,representnilexplicitlyingeneratedcontent,properties%29.md)
  Creates an object schema.
- [init(referenceTo: String)](./init%28referenceto%29.md)
  Creates a reference schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](./init%28type,guides%29.md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](./property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(arrayof:minimumelements:maximumelements:))*