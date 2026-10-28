# init(name:description:type:guides:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an optional property that contains a generable type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init<Value>(name: String, description: String? = nil, type: Value?.Type, guides: [GenerationGuide<Value>] = []) where Value : Generable
```

**Other overloads**:

```swift
init<RegexOutput>(name: String, description: String? = nil, type: String.Type, guides: [Regex<RegexOutput>] = [])
```

```swift
init<RegexOutput>(name: String, description: String? = nil, type: String?.Type, guides: [Regex<RegexOutput>] = [])
```

```swift
init<Value>(name: String, description: String? = nil, type: Value.Type, guides: [GenerationGuide<Value>] = []) where Value : Generable
```

## Parameters

- `name`: The property’s name.
- `description`: A natural language description of what content should be generated for this property.
- `type`: The type this property represents.
- `guides`: A list of guides to apply to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/property/init(name:description:type:guides:)-1w5sd)*