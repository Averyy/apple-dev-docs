# OrdinalEncoder.Transformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that encodes a category as an integer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct Transformer
```

## Topics

### Creating a transformer
- [init(categories: Set<Category?>)](ordinalencoder/transformer/init(categories:).md)
  Creates an ordinal encoder.
### Getting the categories
- [var categories: Set<Category?>](ordinalencoder/transformer/categories.md)
  Unique values to encode
- [func category(at: Int) -> Category?](ordinalencoder/transformer/category(at:).md)
  Retrieves the category at the ordinal encoding index.
### Applying the transformation
- [func applied<S>(S, eventHandler: EventHandler?) throws -> [Int]](ordinalencoder/transformer/applied(_:eventhandler:).md)
  Performs an ordinal encoding on a sequence of inputs.
- [func applied(to: Category?, eventHandler: EventHandler?) throws -> Int](ordinalencoder/transformer/applied(to:eventhandler:).md)
  Performs an ordinal encoding on a single input.
### Default Implementations
- [Decodable Implementations](ordinalencoder/transformer/decodable-implementations.md)
- [Encodable Implementations](ordinalencoder/transformer/encodable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/transformer)*