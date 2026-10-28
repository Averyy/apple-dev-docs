---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedalltoshardedlinear"
framework: "mlx-swift/MLXNN"
---

# QuantizedAllToShardedLinear

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

The quantized flavor of [`AllToShardedLinear`](./alltoshardedlinear.md).

## Declaration

```swift
class QuantizedAllToShardedLinear
```

## Overview

Like [`QuantizedLinear`](./quantizedlinear.md) its parameters are frozen.

## Topics

### Initializers
- [convenience init(QuantizedLinear, segments: Segments, group: MLXDistributed.Group?) throws](./quantizedalltoshardedlinear/init%28_,segments,group%29.md)
  Create a sharded layer from an existing [`QuantizedLinear`](./quantizedlinear.md).
- [init(shardedWeight: MLXArray, bias: MLXArray?, groupSize: Int, bits: Int, mode: QuantizationMode, group: MLXDistributed.Group)](./quantizedalltoshardedlinear/init%28shardedweight,bias,groupsize,bits,mode,group%29.md)
  Quantize a weight that is already this process’ shard.
### Instance Properties
- [let group: MLXDistributed.Group](./quantizedalltoshardedlinear/group.md)
  The group the output dimensions are sharded across.
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./quantizedalltoshardedlinear/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [QuantizedLinear](./quantizedlinear.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [Quantizable](./quantizable.md)
- [Quantized](./quantized.md)
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedalltoshardedlinear)*