---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/alltoshardedlinear/init(_:_:bias:group:)"
framework: "mlx-swift/MLXNN"
---

# init(_:_:bias:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(_ inputDimensions: Int, _ outputDimensions: Int, bias: Bool = true, group: MLXDistributed.Group? = nil) throws
```

## Parameters

- `inputDimensions`: Number of input dimensions
- `outputDimensions`: Number of output dimensions, sharded across the group
- `bias`: If `true` this layer will apply a bias
- `group`: The group to shard across, or `nil` to use the global group


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/alltoshardedlinear/init(_:_:bias:group:))*