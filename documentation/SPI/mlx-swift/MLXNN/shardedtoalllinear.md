---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardedtoalllinear"
framework: "mlx-swift/MLXNN"
---

# ShardedToAllLinear

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Each member of the group applies part of the affine transformation and the results are then aggregated.

## Declaration

```swift
class ShardedToAllLinear
```

## Overview

Every member of the group ends up with the same result.

This is a [`Linear`](./linear.md), so it can replace one in a model.

## Topics

### Initializers
- [init(Int, Int, bias: Bool, group: MLXDistributed.Group?) throws](./shardedtoalllinear/init%28_,_,bias,group%29.md)
- [convenience init(Linear, segments: Segments, group: MLXDistributed.Group?) throws](./shardedtoalllinear/init%28_,segments,group%29.md)
  Create a sharded layer from an existing [`Linear`](./linear.md).
### Instance Properties
- [let group: MLXDistributed.Group](./shardedtoalllinear/group.md)
  The group the input dimensions are sharded across.
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./shardedtoalllinear/callasfunction%28_%29.md)
- [func toQuantized(groupSize: Int, bits: Int, mode: QuantizationMode) -> Module](./shardedtoalllinear/toquantized%28groupsize,bits,mode%29.md)
  Quantizing keeps the layer sharded.

## Relationships

### Inherits From
- [Linear](./linear.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [Quantizable](./quantizable.md)
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardedtoalllinear)*