# BNNS.Layer

**Framework**: Accelerate  
**Kind**: class

The base class for layer objects that wrap filters and manage deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
class Layer
```

## Topics

### Instance Properties
- [let bnnsFilter: BNNSFilter](bnns/layer/bnnsfilter.md)
  The underlying filter.

## Relationships

### Inherited By
- [BNNS.BinaryArithmeticLayer](bnns/binaryarithmeticlayer.md)
- [BNNS.BinaryLayer](bnns/binarylayer.md)
- [BNNS.BroadcastMatrixMultiplyLayer](bnns/broadcastmatrixmultiplylayer.md)
- [BNNS.EmbeddingLayer](bnns/embeddinglayer.md)
- [BNNS.FusedLayer](bnns/fusedlayer.md)
- [BNNS.LossLayer](bnns/losslayer.md)
- [BNNS.NormalizationLayer](bnns/normalizationlayer.md)
- [BNNS.PoolingLayer](bnns/poolinglayer.md)
- [BNNS.TernaryArithmeticLayer](bnns/ternaryarithmeticlayer.md)
- [BNNS.UnaryArithmeticLayer](bnns/unaryarithmeticlayer.md)
- [BNNS.UnaryLayer](bnns/unarylayer.md)

## See Also

- [class UnaryLayer](bnns/unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](bnns/binarylayer.md)
  The base class for layers that accept two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/layer)*