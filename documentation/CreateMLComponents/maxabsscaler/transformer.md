# MaxAbsScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

An transformer that scales the input values so that the maximum absolute value is 1.0.

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
- [init(maximumAbsoluteValue: Element)](maxabsscaler/transformer/init(maximumabsolutevalue:).md)
  Creates a max abs scaling transformer.
### Getting the absolute value
- [var maximumAbsoluteValue: Element](maxabsscaler/transformer/maximumabsolutevalue.md)
  The fitted maximum absolute value.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](maxabsscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values by `1 / maximumAbsoluteValue`.
### Operators
- [static func == (MaxAbsScaler<Element>.Transformer, MaxAbsScaler<Element>.Transformer) -> Bool](maxabsscaler/transformer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](maxabsscaler/transformer/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](maxabsscaler/transformer/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MaxAbsScaler.Transformer.Input](maxabsscaler/transformer/input.md)
  The input type.
- [MaxAbsScaler.Transformer.Output](maxabsscaler/transformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](maxabsscaler/transformer/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](maxabsscaler/transformer/decodable-implementations.md)
- [Encodable Implementations](maxabsscaler/transformer/encodable-implementations.md)
- [Equatable Implementations](maxabsscaler/transformer/equatable-implementations.md)
- [Transformer Implementations](maxabsscaler/transformer/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/maxabsscaler/transformer)*