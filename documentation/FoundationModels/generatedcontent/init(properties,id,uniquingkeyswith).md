# init(properties:id:uniquingKeysWith:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates generated content from key-value pairs, resolving duplicate keys with a combining closure.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init<S>(properties: S, id: GenerationID? = nil, uniquingKeysWith combine: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows where S : Sequence, S.Element == (String, any ConvertibleToGeneratedContent)
```

## Discussion

The order of properties is important. For [`Generable`](../generable.md) types, the order must match the order properties in the types `schema`.

You use this initializer to create generated content when you have a sequence of key-value tuples that might have duplicate keys. As the content is built, the initializer calls the `combine` closure with the current and new values for any duplicate keys. Pass a closure as `combine` that returns the value to use in the resulting content: The closure can choose between the two values, combine them to produce a new value, or even throw an error.

The following example shows how to choose the first and last values for any duplicate keys:

```swift
    let content = GeneratedContent(
      properties: [("name", "John"), ("name", "Jane"), ("married", true)],
      uniquingKeysWith: { (first, _) in first }
    )
    // GeneratedContent(["name": "John", "married": true])
```

## Parameters

- `properties`: A sequence of key-value pairs to use for the new content.
- `id`: A unique id associated with [`GeneratedContent`](../generatedcontent.md).
- `combine`: A closure that is called with the values to resolve any duplicates keys that are encountered. The closure returns the desired value for the final content.

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
- [init(json: String) throws](./init%28json%29.md)
  Creates equivalent content from a JSON string.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](./init%28kind,id%29.md)
  Creates content with the specified kind and generation identifier.
- [GeneratedContent.ParsingError](./parsingerror.md)
  A failure that occurs when a string cannot be parsed into generated content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(properties:id:uniquingkeyswith:))*