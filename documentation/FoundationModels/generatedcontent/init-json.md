# init(json:)

**Framework**: Foundation Models  
**Kind**: init

Creates equivalent content from a JSON string.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(json: String) throws
```

#### Discussion

The JSON string you provide may be incomplete. This is useful for correctly handling partially generated responses.

```swift
@Generable struct NovelIdea {
  let title: String
}

let partial = #"{"title": "A story of"#
let content = try GeneratedContent(json: partial)
let idea = try NovelIdea(content)
print(idea.title) // A story of
```

## See Also

- [init(_:)](generatedcontent/init(_:).md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](generatedcontent/init(_:id:).md)
  Creates content that contains a single value with a custom `GenerationID`.
- [init<S>(elements: S, id: GenerationID?)](generatedcontent/init(elements:id:).md)
  Creates content representing an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](generatedcontent/init(properties:id:).md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](generatedcontent/init(properties:id:uniquingkeyswith:).md)
  Creates new generated content from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](generatedcontent/init(kind:id:).md)
  Creates a new `GeneratedContent` instance with the specified kind and `GenerationID`.
- [GeneratedContent.ParsingError](generatedcontent/parsingerror.md)
  A failure that occurs when a string cannot be parsed into GeneratedContent.
- [static let null: GeneratedContent](generatedcontent/null.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(json:))*