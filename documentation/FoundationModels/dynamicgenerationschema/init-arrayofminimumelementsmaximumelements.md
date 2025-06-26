# init(arrayOf:minimumElements:maximumElements:)

**Framework**: Foundation Models  
**Kind**: init

Creates an array schema.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(arrayOf itemSchema: DynamicGenerationSchema, minimumElements: Int? = nil, maximumElements: Int? = nil)
```

## See Also

- [init(name:description:anyOf:)](dynamicgenerationschema/init(name:description:anyof:).md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](dynamicgenerationschema/init(name:description:properties:).md)
  Creates an object schema.
- [init(referenceTo: String)](dynamicgenerationschema/init(referenceto:).md)
  Creates an refrence schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](dynamicgenerationschema/init(type:guides:).md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](dynamicgenerationschema/property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(arrayof:minimumelements:maximumelements:))*