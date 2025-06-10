# NormalizationScaler.NormalizationStrategy

**Framework**: Create ML Components  
**Kind**: enum

A normalization strategy.

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
enum NormalizationStrategy
```

## Topics

### Normalization strategies
- [NormalizationScaler.NormalizationStrategy.l1](normalizationscaler/normalizationstrategy/l1.md)
  A normalization strategy that scales by the L1 Norm (sum of vector absolute values).
- [NormalizationScaler.NormalizationStrategy.l2](normalizationscaler/normalizationstrategy/l2.md)
  A normalization strategy that scales by the L2 Norm (Euclidean norm).
### Operators
- [static func == (NormalizationScaler<Element>.NormalizationStrategy, NormalizationScaler<Element>.NormalizationStrategy) -> Bool](normalizationscaler/normalizationstrategy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](normalizationscaler/normalizationstrategy/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](normalizationscaler/normalizationstrategy/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](normalizationscaler/normalizationstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(norm: NormalizationScaler<Element>.NormalizationStrategy)](normalizationscaler/init(norm:).md)
  Creates a normalization scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/normalizationstrategy)*