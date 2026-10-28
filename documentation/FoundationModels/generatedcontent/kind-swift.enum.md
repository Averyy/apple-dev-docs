# GeneratedContent.Kind

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

A representation of the different types of content that can be stored in generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
enum Kind
```

## Overview

`Kind` represents the various types of JSON-compatible data that can be held within a [`GeneratedContent`](../generatedcontent.md) instance, including primitive types, arrays, and structured objects.

## Topics

### Getting the kind of content
- [GeneratedContent.Kind.array(_:)](./kind-swift.enum/array%28_%29.md)
  An array of generated content elements.
- [GeneratedContent.Kind.bool(_:)](./kind-swift.enum/bool%28_%29.md)
  A boolean value.
- [GeneratedContent.Kind.null](./kind-swift.enum/null.md)
  A null value.
- [GeneratedContent.Kind.number(_:)](./kind-swift.enum/number%28_%29.md)
  A numeric value.
- [GeneratedContent.Kind.string(_:)](./kind-swift.enum/string%28_%29.md)
  A string value.
- [case structure(properties: [String : GeneratedContent], orderedKeys: [String])](./kind-swift.enum/structure%28properties,orderedkeys%29.md)
  A structured object with key-value pairs.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the content
- [var kind: GeneratedContent.Kind](./kind-swift.property.md)
  The representation of the generated content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/kind-swift.enum)*