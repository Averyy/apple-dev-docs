# GeneratedContent.Kind

**Framework**: Foundation Models  
**Kind**: enum

A representation of the different types of content that can be stored in generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Kind
```

#### Overview

`Kind` represents the various types of JSON-compatible data that can be held within a [`GeneratedContent`](generatedcontent.md) instance, including primitive types, arrays, and structured objects.

## Topics

### Getting the kind of content
- [GeneratedContent.Kind.array(_:)](generatedcontent/kind-swift.enum/array(_:).md)
  Represents an array of `GeneratedContent` elements.
- [GeneratedContent.Kind.bool(_:)](generatedcontent/kind-swift.enum/bool(_:).md)
  Represents a boolean value.
- [GeneratedContent.Kind.null](generatedcontent/kind-swift.enum/null.md)
  Represents a null value.
- [GeneratedContent.Kind.number(_:)](generatedcontent/kind-swift.enum/number(_:).md)
  Represents a numeric value.
- [GeneratedContent.Kind.string(_:)](generatedcontent/kind-swift.enum/string(_:).md)
  Represents a string value.
- [case structure(properties: [String : GeneratedContent], orderedKeys: [String])](generatedcontent/kind-swift.enum/structure(properties:orderedkeys:).md)
  Represents a structured object with key-value pairs.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var kind: GeneratedContent.Kind](generatedcontent/kind-swift.property.md)
  The representation of the generated content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/kind-swift.enum)*