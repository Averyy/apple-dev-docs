# init(properties:id:)

**Framework**: Foundation Models  
**Kind**: init

Creates generated content representing a structure with the properties you specify.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID? = nil)
```

#### Discussion

The order of properties is important. For [`Generable`](generable.md) types, the order must match the order properties in the types `schema`.

## See Also

- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](generatedcontent/init(properties:id:uniquingkeyswith:).md)
  Creates new generated content from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(properties:id:))*