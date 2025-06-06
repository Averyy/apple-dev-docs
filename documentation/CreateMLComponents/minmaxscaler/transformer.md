# MinMaxScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that scales the input values so that they all lie in a closed range.

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
- [init(desiredRange: ClosedRange<Element>, fittedRange: ClosedRange<Element>)](minmaxscaler/transformer/init(desiredrange:fittedrange:).md)
  Creates a minmax scaling transformer.
### Getting the properties
- [var desiredRange: ClosedRange<Element>](minmaxscaler/transformer/desiredrange.md)
  The desired range of transformed values.
- [var fittedRange: ClosedRange<Element>](minmaxscaler/transformer/fittedrange.md)
  The fitted range derived by the estimator when fitting.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](minmaxscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values so that they all lie in the closed range `[minimum, maximum]`.
### Operators
- [static func == (MinMaxScaler<Element>.Transformer, MinMaxScaler<Element>.Transformer) -> Bool](minmaxscaler/transformer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](minmaxscaler/transformer/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](minmaxscaler/transformer/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MinMaxScaler.Transformer.Input](minmaxscaler/transformer/input.md)
  The input type.
- [MinMaxScaler.Transformer.Output](minmaxscaler/transformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](minmaxscaler/transformer/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](minmaxscaler/transformer/decodable-implementations.md)
- [Encodable Implementations](minmaxscaler/transformer/encodable-implementations.md)
- [Equatable Implementations](minmaxscaler/transformer/equatable-implementations.md)
- [Transformer Implementations](minmaxscaler/transformer/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler/transformer)*