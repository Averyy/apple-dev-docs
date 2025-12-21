# jsonString

**Framework**: Foundation Models  
**Kind**: property

Returns a JSON string representation of the generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var jsonString: String { get }
```

#### Examples

```swift
// Object with properties
let content = GeneratedContent(properties: [
    "name": "Johnny Appleseed",
    "age": 30,
])
print(content.jsonString)
// Output: {"name": "Johnny Appleseed", "age": 30}
```

## See Also

- [var kind: GeneratedContent.Kind](generatedcontent/kind-swift.property.md)
  The kind representation of this generated content.
- [var isComplete: Bool](generatedcontent/iscomplete.md)
  A Boolean that indicates whether the generated content is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/jsonstring)*