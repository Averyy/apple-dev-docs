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
- watchOS 27.0+ (Beta)

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
  The representation of the generated content.
- [GeneratedContent.Kind](generatedcontent/kind-swift.enum.md)
  A representation of the different types of content that can be stored in generated content.
- [func value<Value>(Value.Type) throws -> Value](generatedcontent/value(_:).md)
  Reads a top level, concrete partially `Generable` type from a named property.
- [func value(_:forProperty:)](generatedcontent/value(_:forproperty:).md)
  Reads a concrete `Generable` type from named property.
- [var isComplete: Bool](generatedcontent/iscomplete.md)
  A Boolean that indicates whether the generated content is completed.
- [var generatedContent: GeneratedContent](generatedcontent/generatedcontent.md)
  A representation of this instance.
- [var debugDescription: String](generatedcontent/debugdescription.md)
  A string representation for the debug description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/jsonstring)*