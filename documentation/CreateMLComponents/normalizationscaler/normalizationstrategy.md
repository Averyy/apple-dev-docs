# NormalizationScaler.NormalizationStrategy

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

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
- [NormalizationScaler.NormalizationStrategy.l1](./normalizationstrategy/l1.md)
  A normalization strategy that scales by the L1 Norm (sum of vector absolute values).
- [NormalizationScaler.NormalizationStrategy.l2](./normalizationstrategy/l2.md)
  A normalization strategy that scales by the L2 Norm (Euclidean norm).

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a scaler
- [init(norm: NormalizationScaler<Element>.NormalizationStrategy)](./init%28norm%29.md)
  Creates a normalization scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/normalizationstrategy)*