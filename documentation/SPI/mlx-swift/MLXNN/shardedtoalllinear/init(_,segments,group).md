---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardedtoalllinear/init(_:segments:group:)"
framework: "mlx-swift/MLXNN"
---

# init(_:segments:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Create a sharded layer from an existing [`Linear`](../linear.md).

## Declaration

```swift
convenience init(_ other: Linear, segments: Segments = .count(1), group: MLXDistributed.Group? = nil) throws
```

## Discussion

Throws for a [`QuantizedLinear`](../quantizedlinear.md): shard it with [`shardLinear(_:sharding:segments:group:)`](../shardlinear%28_,sharding,segments,group%29.md) or [`QuantizedShardedToAllLinear`](../quantizedshardedtoalllinear.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardedtoalllinear/init(_:segments:group:))*