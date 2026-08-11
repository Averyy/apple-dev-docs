# init(elements:id:)

**Framework**: Foundation Models  
**Kind**: init

Creates content representing an array of elements you specify.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
init<S>(elements: S, id: GenerationID? = nil) where S : Sequence, S.Element == any ConvertibleToGeneratedContent
```

## See Also

- [init(_:)](generatedcontent/init(_:).md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](generatedcontent/init(_:id:).md)
  Creates content that contains a single value with a custom generation identifier.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](generatedcontent/init(properties:id:).md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](generatedcontent/init(properties:id:uniquingkeyswith:).md)
  Creates generated content from key-value pairs, resolving duplicate keys with a combining closure.
- [init(json: String) throws](generatedcontent/init(json:).md)
  Creates equivalent content from a JSON string.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](generatedcontent/init(kind:id:).md)
  Creates content with the specified kind and generation identifier.
- [GeneratedContent.ParsingError](generatedcontent/parsingerror.md)
  A failure that occurs when a string cannot be parsed into GeneratedContent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(elements:id:))*