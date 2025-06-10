# StandardScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that standardizes the input by removing the mean and scaling to unit variance.

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
- [init(mean: Element, standardDeviation: Element)](standardscaler/transformer/init(mean:standarddeviation:).md)
  Creates a standard scaling transformer.
### Getting the properties
- [var mean: Element](standardscaler/transformer/mean.md)
  The mean used for offsetting.
- [var standardDeviation: Element](standardscaler/transformer/standarddeviation.md)
  The standard deviation used for scaling.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](standardscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values using the calculation `(input - mean) / standardDeviation`.
### Operators
- [static func == (StandardScaler<Element>.Transformer, StandardScaler<Element>.Transformer) -> Bool](standardscaler/transformer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](standardscaler/transformer/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](standardscaler/transformer/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [StandardScaler.Transformer.Input](standardscaler/transformer/input.md)
  The input type.
- [StandardScaler.Transformer.Output](standardscaler/transformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](standardscaler/transformer/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](standardscaler/transformer/decodable-implementations.md)
- [Encodable Implementations](standardscaler/transformer/encodable-implementations.md)
- [Equatable Implementations](standardscaler/transformer/equatable-implementations.md)
- [Transformer Implementations](standardscaler/transformer/transformer-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/transformer)*