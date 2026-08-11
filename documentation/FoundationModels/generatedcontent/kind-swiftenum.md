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
  An array of generated content elements.
- [GeneratedContent.Kind.bool(_:)](generatedcontent/kind-swift.enum/bool(_:).md)
  A boolean value.
- [GeneratedContent.Kind.null](generatedcontent/kind-swift.enum/null.md)
  A null value.
- [GeneratedContent.Kind.number(_:)](generatedcontent/kind-swift.enum/number(_:).md)
  A numeric value.
- [GeneratedContent.Kind.string(_:)](generatedcontent/kind-swift.enum/string(_:).md)
  A string value.
- [case structure(properties: [String : GeneratedContent], orderedKeys: [String])](generatedcontent/kind-swift.enum/structure(properties:orderedkeys:).md)
  A structured object with key-value pairs.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var kind: GeneratedContent.Kind](generatedcontent/kind-swift.property.md)
  The representation of the generated content.
- [func value<Value>(Value.Type) throws -> Value](generatedcontent/value(_:).md)
  Reads a top level, concrete partially generable type from a named property.
- [func value(_:forProperty:)](generatedcontent/value(_:forproperty:).md)
  Reads a concrete generable type from a named property.
- [var isComplete: Bool](generatedcontent/iscomplete.md)
  A Boolean value that indicates whether the generated content is complete.
- [var generatedContent: GeneratedContent](generatedcontent/generatedcontent.md)
  A representation of this instance.
- [var jsonString: String](generatedcontent/jsonstring.md)
  A JSON string representation of the generated content.
- [var debugDescription: String](generatedcontent/debugdescription.md)
  A string representation for the debug description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/kind-swift.enum)*