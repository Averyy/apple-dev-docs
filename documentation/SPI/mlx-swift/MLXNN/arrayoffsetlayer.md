---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/arrayoffsetlayer"
framework: "mlx-swift/MLXNN"
---

# ArrayOffsetLayer

**Framework**: mlx-swift/MLXNN  
**Kind**: protocol  
**Role**: Protocol

A layer ([`Module`](./module.md) subclass) that can be evaluated with an input array and a per-example position offset.

## Declaration

```swift
protocol ArrayOffsetLayer : Module
```

#### Overview

Use this for batched inference when each sequence in the batch may be at a different position in the prompt. The `offset` is provided as an `MLXArray` so it can be:

- a scalar (one offset applied to the whole batch), or
- a vector of length `batchSize` (one offset per sequence).

Layers that support this protocol should broadcast the `offset` over the remaining dimensions of `x` as appropriate.

## Topics

### Instance Methods
- [func callAsFunction(MLXArray, offset: MLXArray) -> MLXArray](./arrayoffsetlayer/callasfunction%28_,offset%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforming Types
- [RoPE](./rope.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/arrayoffsetlayer)*