---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardlinear(_:sharding:segments:group:)"
framework: "mlx-swift/MLXNN"
---

# shardLinear(_:sharding:segments:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Create a new linear layer with sharded parameters that also performs the distributed communication, either in the forward or the backward pass.

## Declaration

```swift
func shardLinear(_ layer: Linear, sharding: ShardingType, segments: Segments = .count(1), group: MLXDistributed.Group? = nil) throws -> Linear
```

## Return Value

The sharded layer, which can replace `layer` in a model

## Discussion

Unlike [`shardInPlace(_:sharding:segments:group:)`](./shardinplace%28_,sharding,segments,group%29.md) the original layer is not changed.  A [`QuantizedLinear`](./quantizedlinear.md) yields the quantized flavor of the sharded layer, so a quantized model shards like any other.

## Parameters

- `layer`: The linear layer to shard
- `sharding`: The kind of sharding to apply
- `segments`: The segments that comprise each unsharded weight
- `group`: The group to shard across, or `nil` to use the global group


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardlinear(_:sharding:segments:group:))*