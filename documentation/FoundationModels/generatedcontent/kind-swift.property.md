# kind

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The representation of the generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
var kind: GeneratedContent.Kind { get }
```

## Discussion

This property provides access to the content in a strongly-typed enumeration representation, preserving the hierarchical structure of the data and the data’s [`GenerationID`](../generationid.md) values.

## See Also

### Accessing the content
- [GeneratedContent.Kind](./kind-swift.enum.md)
  A representation of the different types of content that can be stored in generated content.
- [func value<Value>(Value.Type) throws -> Value](./value%28_%29.md)
  Reads a top level, concrete partially generable type from a named property.
- [func value(_:forProperty:)](./value%28_,forproperty%29.md)
  Reads a concrete generable type from a named property.
- [var isComplete: Bool](./iscomplete.md)
  A Boolean value that indicates whether the generated content is complete.
- [var generatedContent: GeneratedContent](./generatedcontent.md)
  A representation of this instance.
- [var jsonString: String](./jsonstring.md)
  A JSON string representation of the generated content.
- [var debugDescription: String](./debugdescription.md)
  A string representation for the debug description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/kind-swift.property)*