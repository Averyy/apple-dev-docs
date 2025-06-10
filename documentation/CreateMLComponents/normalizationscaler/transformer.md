# NormalizationScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that scales the input using a normalization strategy.

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
- [init(scale: Element)](normalizationscaler/transformer/init(scale:).md)
  Creates a normalization scaling transformer.
### Getting the scale
- [var scale: Element](normalizationscaler/transformer/scale.md)
  The normalization scale used to scale the input.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](normalizationscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values using the calculation `input / scale`.
### Operators
- [static func == (NormalizationScaler<Element>.Transformer, NormalizationScaler<Element>.Transformer) -> Bool](normalizationscaler/transformer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](normalizationscaler/transformer/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](normalizationscaler/transformer/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [NormalizationScaler.Transformer.Input](normalizationscaler/transformer/input.md)
  The input type.
- [NormalizationScaler.Transformer.Output](normalizationscaler/transformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](normalizationscaler/transformer/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](normalizationscaler/transformer/decodable-implementations.md)
- [Encodable Implementations](normalizationscaler/transformer/encodable-implementations.md)
- [Equatable Implementations](normalizationscaler/transformer/equatable-implementations.md)
- [Transformer Implementations](normalizationscaler/transformer/transformer-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/transformer)*