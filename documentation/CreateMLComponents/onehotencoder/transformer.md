# OneHotEncoder.Transformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that encodes a category as an array of integers.

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
- [init(categories: Set<Category?>)](onehotencoder/transformer/init(categories:).md)
  Creates a one-hot encoder.
### Getting the categories
- [var categories: Set<Category?>](onehotencoder/transformer/categories.md)
  Unique values to encode
- [func category(at: Int) -> Category?](onehotencoder/transformer/category(at:).md)
  Retrieves the category at the one-hot encoding index.
### Performing the transformation
- [func applied<S>(S, eventHandler: EventHandler?) throws -> [[Int]]](onehotencoder/transformer/applied(_:eventhandler:).md)
  Performs a one-hot encoding on a sequence of inputs.
- [func applied(to: Category?, eventHandler: EventHandler?) throws -> [Int]](onehotencoder/transformer/applied(to:eventhandler:).md)
  Performs a one-hot encoding on a single input.
### Default Implementations
- [Decodable Implementations](onehotencoder/transformer/decodable-implementations.md)
- [Encodable Implementations](onehotencoder/transformer/encodable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/transformer)*