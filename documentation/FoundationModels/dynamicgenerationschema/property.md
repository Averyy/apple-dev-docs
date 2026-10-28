# DynamicGenerationSchema.Property

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A property that belongs to a dynamic generation schema.

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

## Overview

Fields are named members of object types. Fields are strongly typed and have optional descriptions.

## Topics

### Creating a property
- [init(name: String, description: String?, schema: DynamicGenerationSchema, isOptional: Bool)](./property/init%28name,description,schema,isoptional%29.md)
  Creates a property referencing a dynamic schema.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [init<Value>(type: Value.Type, guides: [GenerationGuide<Value>])](./init%28type,guides%29.md)
  Creates a schema from a generable type and guides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/property)*