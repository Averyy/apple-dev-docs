# init(name:description:type:guides:)

**Framework**: Foundation Models  
**Kind**: init

Create a property that contains a string type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init<RegexOutput>(name: String, description: String? = nil, type: String.Type, guides: [Regex<RegexOutput>] = [])
```

## Parameters

- `name`: The property’s name.
- `description`: A natural language description of what content   should be generated for this property.
- `type`: The type this property represents.
- `guides`: An array of regexes to be applied to this string. If there’re multiple regexes in the array, only the last one will be applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/property/init(name:description:type:guides:))*