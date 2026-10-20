# BNNS.Layer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

The base class for layer objects that wrap filters and manage deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class Layer
```

## Topics

### Instance Properties
- [let bnnsFilter: BNNSFilter](./layer/bnnsfilter.md)
  The underlying filter.

## Relationships

### Inherited By
- [BNNS.BinaryArithmeticLayer](./binaryarithmeticlayer.md)
- [BNNS.BinaryLayer](./binarylayer.md)
- [BNNS.BroadcastMatrixMultiplyLayer](./broadcastmatrixmultiplylayer.md)
- [BNNS.EmbeddingLayer](./embeddinglayer.md)
- [BNNS.FusedLayer](./fusedlayer.md)
- [BNNS.LossLayer](./losslayer.md)
- [BNNS.NormalizationLayer](./normalizationlayer.md)
- [BNNS.PoolingLayer](./poolinglayer.md)
- [BNNS.TernaryArithmeticLayer](./ternaryarithmeticlayer.md)
- [BNNS.UnaryArithmeticLayer](./unaryarithmeticlayer.md)
- [BNNS.UnaryLayer](./unarylayer.md)

## See Also

### Base Classes
- [class UnaryLayer](./unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](./binarylayer.md)
  The base class for layers that accept two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/layer)*