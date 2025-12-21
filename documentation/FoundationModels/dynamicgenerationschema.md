# DynamicGenerationSchema

**Framework**: Foundation Models  
**Kind**: struct

The dynamic counterpart to the generation schema type that you use to construct schemas at runtime.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DynamicGenerationSchema
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

An individual schema may reference other schemas by name, and references are resolved when converting a set of dynamic schemas into a [`GenerationSchema`](generationschema.md).

## Topics

### Creating a dynamic schema
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
- [DynamicGenerationSchema.Property](dynamicgenerationschema/property.md)
  A property that belongs to a dynamic generation schema.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema)*