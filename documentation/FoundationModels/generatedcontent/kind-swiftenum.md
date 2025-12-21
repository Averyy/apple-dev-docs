# GeneratedContent.Kind

**Framework**: Foundation Models  
**Kind**: enum

The representation of the generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Kind
```

#### Overview

This property provides access to the content in a strongly-typed enumeration representation, preserving the hierarchical structure of the data and the data’s [`GenerationID`](generationid.md) values.

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

- [init(kind: GeneratedContent.Kind, id: GenerationID?)](generatedcontent/init(kind:id:).md)
  Creates a new `GeneratedContent` instance with the specified kind and `GenerationID`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/kind-swift.enum)*