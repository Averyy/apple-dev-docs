# init(name:description:anyOf:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an enum schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(name: String, description: String? = nil, anyOf choices: [String])
```

**Other overloads**:

```swift
init(name: String, description: String? = nil, anyOf choices: [DynamicGenerationSchema])
```

## Parameters

- `name`: A name this schema can be referenced by.
- `description`: A natural language description of this [`DynamicGenerationSchema`](../dynamicgenerationschema.md).
- `choices`: An array of strings this one will be a union of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/init(name:description:anyof:)-14d08)*