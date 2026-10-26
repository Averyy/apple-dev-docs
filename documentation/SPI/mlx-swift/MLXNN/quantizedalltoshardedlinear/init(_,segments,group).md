---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedalltoshardedlinear/init(_:segments:group:)"
framework: "mlx-swift/MLXNN"
---

# init(_:segments:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Create a sharded layer from an existing [`QuantizedLinear`](../quantizedlinear.md).

## Declaration

```swift
convenience init(_ other: QuantizedLinear, segments: Segments = .count(1), group: MLXDistributed.Group? = nil) throws
```

#### Discussion

The packed weight, `scales` and `biases` all carry one row per output, so they shard together along the output dimension.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedalltoshardedlinear/init(_:segments:group:))*