---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardingpredicate"
framework: "mlx-swift/MLXNN"
---

# ShardingPredicate

**Framework**: mlx-swift/MLXNN  
**Kind**: typealias  
**Role**: Type Alias

The sharding axis and segments for a parameter, or `nil` to leave it alone.

## Declaration

```swift
typealias ShardingPredicate = (String, MLXArray) -> (axis: Int, segments: Segments)?
```

## Discussion

The path is the parameter’s path in the module, e.g. `layers.0.conv.weight`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardingpredicate)*