# init(name:description:properties:)

**Framework**: Foundation Models  
**Kind**: init

Creates an object schema.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(name: String, description: String? = nil, properties: [DynamicGenerationSchema.Property])
```

## Parameters

- `name`: A name this dynamic schema can be referenced by.
- `description`: A natural language description of this schema.
- `properties`: The properties to associated with this schema.

## See Also

- [init(arrayOf: DynamicGenerationSchema, minimumElements: Int?, maximumElements: Int?)](dynamicgenerationschema/init(arrayof:minimumelements:maximumelements:).md)
  Creates an array schema.
- [init(dictionaryOf: DynamicGenerationSchema)](dynamicgenerationschema/init(dictionaryof:).md)
  Creates a dictionary schema.
- [init(name:description:anyOf:)](dynamicgenerationschema/init(name:description:anyof:).md)
  Creates an any-of schema.
- [init(referenceTo: String)](dynamicgenerationschema/init(referenceto:).md)
  Creates an refrence schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](dynamicgenerationschema/init(type:guides:).md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](dynamicgenerationschema/property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(name:description:properties:))*