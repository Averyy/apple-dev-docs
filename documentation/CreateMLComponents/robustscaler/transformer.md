# RobustScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that scales the input using statistics that are robust to outliers.

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
- [init(median: Element, interQuartileRange: Element)](robustscaler/transformer/init(median:interquartilerange:).md)
  Creates a robust scaling transformer.
### Getting the properties
- [var interQuartileRange: Element](robustscaler/transformer/interquartilerange.md)
  The interquartile rage  used for scaling.
- [var median: Element](robustscaler/transformer/median.md)
  The median used for offsetting.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](robustscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values using the calculation `(input - median) / interQuartileRange`.
### Operators
- [static func == (RobustScaler<Element>.Transformer, RobustScaler<Element>.Transformer) -> Bool](robustscaler/transformer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](robustscaler/transformer/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](robustscaler/transformer/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [RobustScaler.Transformer.Input](robustscaler/transformer/input.md)
  The input type.
- [RobustScaler.Transformer.Output](robustscaler/transformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](robustscaler/transformer/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](robustscaler/transformer/decodable-implementations.md)
- [Encodable Implementations](robustscaler/transformer/encodable-implementations.md)
- [Equatable Implementations](robustscaler/transformer/equatable-implementations.md)
- [Transformer Implementations](robustscaler/transformer/transformer-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/robustscaler/transformer)*