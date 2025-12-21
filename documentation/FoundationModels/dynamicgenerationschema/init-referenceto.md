# init(referenceTo:)

**Framework**: Foundation Models  
**Kind**: init

Creates an refrence schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(referenceTo name: String)
```

## Parameters

- `name`: The name of the   this is a reference to.

## See Also

- [init(arrayOf: DynamicGenerationSchema, minimumElements: Int?, maximumElements: Int?)](dynamicgenerationschema/init(arrayof:minimumelements:maximumelements:).md)
  Creates an array schema.
- [init(name:description:anyOf:)](dynamicgenerationschema/init(name:description:anyof:).md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](dynamicgenerationschema/init(name:description:properties:).md)
  Creates an object schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](dynamicgenerationschema/init(type:guides:).md)
  Creates a schema from a generable type and guides.
- [DynamicGenerationSchema.Property](dynamicgenerationschema/property.md)
  A property that belongs to a dynamic generation schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(referenceto:))*