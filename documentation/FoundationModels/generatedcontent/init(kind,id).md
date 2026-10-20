# init(kind:id:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates content with the specified kind and generation identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(kind: GeneratedContent.Kind, id: GenerationID? = nil)
```

#### Discussion

This initializer provides a convenient way to create content from its kind representation.

## Parameters

- `kind`: The kind of content to create.
- `id`: An optional [`GenerationID`](../generationid.md) to associate with this content.

## See Also

### Creating generated content
- [init(_:)](./init%28_%29.md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](./init%28_,id%29.md)
  Creates content that contains a single value with a custom generation identifier.
- [init<S>(elements: S, id: GenerationID?)](./init%28elements,id%29.md)
  Creates content representing an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](./init%28properties,id%29.md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](./init%28properties,id,uniquingkeyswith%29.md)
  Creates generated content from key-value pairs, resolving duplicate keys with a combining closure.
- [init(json: String) throws](./init%28json%29.md)
  Creates equivalent content from a JSON string.
- [GeneratedContent.ParsingError](./parsingerror.md)
  A failure that occurs when a string cannot be parsed into generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(kind:id:))*