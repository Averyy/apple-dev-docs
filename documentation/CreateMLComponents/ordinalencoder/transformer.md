# OrdinalEncoder.Transformer

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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

Available when `Category` conforms to `Comparable`, `Decodable`, `Encodable`, and `Hashable`.

## Topics

### Creating a transformer
- [init(categories: Set<Category?>)](./transformer/init%28categories%29.md)
  Creates an ordinal encoder.
### Getting the categories
- [var categories: Set<Category?>](./transformer/categories.md)
  Unique values to encode
- [func category(at: Int) -> Category?](./transformer/category%28at%29.md)
  Retrieves the category at the ordinal encoding index.
### Applying the transformation
- [func applied<S>(S, eventHandler: EventHandler?) throws -> [Int]](./transformer/applied%28_,eventhandler%29.md)
  Performs an ordinal encoding on a sequence of inputs.
- [func applied(to: Category?, eventHandler: EventHandler?) throws -> Int](./transformer/applied%28to,eventhandler%29.md)
  Performs an ordinal encoding on a single input.
### Default Implementations
- [Decodable Implementations](./transformer/decodable-implementations.md)
- [Encodable Implementations](./transformer/encodable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Transformer](../transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/transformer)*