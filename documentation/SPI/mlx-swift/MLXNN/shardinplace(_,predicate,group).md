---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardinplace(_:predicate:group:)"
framework: "mlx-swift/MLXNN"
---

# shardInPlace(_:predicate:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Shard a module in place, choosing how each parameter is split.

## Declaration

```swift
func shardInPlace(_ module: Module, predicate: (String, MLXArray) -> (axis: Int, segments: Segments)?, group: MLXDistributed.Group? = nil) throws
```

#### Discussion

This is the general form of [`shardInPlace(_:sharding:segments:group:)`](./shardinplace%28_,sharding,segments,group%29.md), and matches what Python’s `shard_inplace` accepts.  The predicate receives a parameter and its path and returns the axis to shard it along, with the segments that make it up, or `nil` to leave the parameter whole.

The module itself is unchanged, so distributed communication only happens if the module supports it natively.

## Parameters

- `module`: The module whose parameters are sharded in place
- `predicate`: Chooses how each parameter is sharded
- `group`: The group to shard across, or `nil` to use the global group


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardinplace(_:predicate:group:))*