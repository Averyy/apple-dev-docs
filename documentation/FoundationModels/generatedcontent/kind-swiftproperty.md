# kind

**Framework**: Foundation Models  
**Kind**: property

The representation of the generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
var kind: GeneratedContent.Kind { get }
```

#### Discussion

This property provides access to the content in a strongly-typed enumeration representation, preserving the hierarchical structure of the data and the data’s [`GenerationID`](generationid.md) values.

## See Also

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
- [var jsonString: String](generatedcontent/jsonstring.md)
  Returns a JSON string representation of the generated content.
- [var debugDescription: String](generatedcontent/debugdescription.md)
  A string representation for the debug description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/kind-swift.property)*