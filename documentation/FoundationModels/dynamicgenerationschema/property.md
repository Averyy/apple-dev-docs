# DynamicGenerationSchema.Property

**Framework**: Foundation Models  
**Kind**: struct

A property that belongs to a dynamic generation schema.

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

Fields are named members of object types. Fields are strongly typed and have optional descriptions.

## Topics

### Creating a property
- [init(name: String, description: String?, schema: DynamicGenerationSchema, isOptional: Bool)](dynamicgenerationschema/property/init(name:description:schema:isoptional:).md)
  Creates a property referencing a dynamic schema.

## See Also

- [init(arrayOf: DynamicGenerationSchema, minimumElements: Int?, maximumElements: Int?)](dynamicgenerationschema/init(arrayof:minimumelements:maximumelements:).md)
  Creates an array schema.
- [init(name:description:anyOf:)](dynamicgenerationschema/init(name:description:anyof:).md)
  Creates an any-of schema.
- [init(name: String, description: String?, properties: [DynamicGenerationSchema.Property])](dynamicgenerationschema/init(name:description:properties:).md)
  Creates an object schema.
- [init(referenceTo: String)](dynamicgenerationschema/init(referenceto:).md)
  Creates an refrence schema.
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](dynamicgenerationschema/init(type:guides:).md)
  Creates a schema from a generable type and guides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/property)*