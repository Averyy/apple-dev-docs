---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantized"
framework: "mlx-swift/MLXNN"
---

# Quantized

**Framework**: mlx-swift/MLXNN  
**Kind**: protocol  
**Role**: Protocol

Protocol for layers that are quantized.

## Declaration

```swift
protocol Quantized : Module
```

## Topics

### Instance Properties
- [var bits: Int](./quantized/bits.md)
- [var groupSize: Int](./quantized/groupsize.md)
- [var mode: QuantizationMode](./quantized/mode.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforming Types
- [QuantizedAllToShardedLinear](./quantizedalltoshardedlinear.md)
- [QuantizedEmbedding](./quantizedembedding.md)
- [QuantizedLinear](./quantizedlinear.md)
- [QuantizedShardedToAllLinear](./quantizedshardedtoalllinear.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantized)*