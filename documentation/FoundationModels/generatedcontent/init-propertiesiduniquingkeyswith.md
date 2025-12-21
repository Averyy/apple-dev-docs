# init(properties:id:uniquingKeysWith:)

**Framework**: Foundation Models  
**Kind**: init

Creates new generated content from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init<S>(properties: S, id: GenerationID? = nil, uniquingKeysWith combine: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows where S : Sequence, S.Element == (String, any ConvertibleToGeneratedContent)
```

#### Discussion

The order of properties is important. For [`Generable`](generable.md) types, the order must match the order properties in the types `schema`.

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
- `id`: A unique id associated with  .
- `combine`: A closure that is called with the values to resolve any duplicates   keys that are encountered. The closure returns the desired value for the final content.

## See Also

- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](generatedcontent/init(properties:id:).md)
  Creates generated content representing a structure with the properties you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(properties:id:uniquingkeyswith:))*