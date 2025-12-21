# init(name:description:schema:isOptional:)

**Framework**: Foundation Models  
**Kind**: init

Creates a property referencing a dynamic schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(name: String, description: String? = nil, schema: DynamicGenerationSchema, isOptional: Bool = false)
```

## Parameters

- `name`: A name for this property.
- `description`: An optional natural language description of this   property’s contents.
- `schema`: A schema representing the type this property contains.
- `isOptional`: Determines if this property is required or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/property/init(name:description:schema:isoptional:))*