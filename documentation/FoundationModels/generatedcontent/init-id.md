# init(_:id:)

**Framework**: Foundation Models  
**Kind**: init

Creates content that contains a single value with a custom `GenerationID`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(_ value: some ConvertibleToGeneratedContent, id: GenerationID)
```

## Parameters

- `value`: The underlying value.
- `id`: The   for this content.

## See Also

- [init(_:)](generatedcontent/init(_:).md)
  Creates generated content from another value.
- [init<S>(elements: S, id: GenerationID?)](generatedcontent/init(elements:id:).md)
  Creates content representing an array of elements you specify.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](generatedcontent/init(kind:id:).md)
  Creates a new `GeneratedContent` instance with the specified kind and `GenerationID`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(_:id:))*