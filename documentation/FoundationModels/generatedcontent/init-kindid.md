# init(kind:id:)

**Framework**: Foundation Models  
**Kind**: init

Creates a new `GeneratedContent` instance with the specified kind and `GenerationID`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(kind: GeneratedContent.Kind, id: GenerationID? = nil)
```

#### Discussion

This initializer provides a convenient way to create content from its kind representation.

## Parameters

- `kind`: The kind of content to create.
- `id`: An optional   to associate with this content.

## See Also

- [init(_:)](generatedcontent/init(_:).md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](generatedcontent/init(_:id:).md)
  Creates content that contains a single value with a custom `GenerationID`.
- [init<S>(elements: S, id: GenerationID?)](generatedcontent/init(elements:id:).md)
  Creates content representing an array of elements you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(kind:id:))*