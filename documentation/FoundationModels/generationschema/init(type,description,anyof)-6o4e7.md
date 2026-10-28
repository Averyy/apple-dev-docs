# init(type:description:anyOf:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a schema as the union of several other types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(type: any Generable.Type, description: String? = nil, anyOf types: [any Generable.Type])
```

**Other overloads**:

```swift
init(type: any Generable.Type, description: String? = nil, anyOf choices: [String])
```

## Parameters

- `type`: The type this schema represents.
- `description`: A natural language description of this schema.
- `types`: The types this schema should be a union of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/init(type:description:anyof:)-6o4e7)*