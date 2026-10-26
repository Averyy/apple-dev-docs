---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardinplace(_:sharding:segments:group:)"
framework: "mlx-swift/MLXNN"
---

# shardInPlace(_:sharding:segments:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Shard a module in place by replacing its parameters with sharded ones.

## Declaration

```swift
func shardInPlace(_ module: Module, sharding: ShardingType, segments: Segments = .count(1), group: MLXDistributed.Group? = nil) throws
```

#### Discussion

The module itself is unchanged, so distributed communication only happens if the module supports it natively.

## Parameters

- `module`: The module whose parameters are sharded in place
- `sharding`: The kind of sharding to apply
- `segments`: The segments that comprise each unsharded weight
- `group`: The group to shard across, or `nil` to use the global group


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardinplace(_:sharding:segments:group:))*