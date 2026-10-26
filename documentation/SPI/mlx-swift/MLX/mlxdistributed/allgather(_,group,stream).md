---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/allgather(_:group:stream:)"
framework: "mlx-swift/MLX"
---

# allGather(_:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Gather arrays from all processes, concatenating along the first axis.

## Declaration

```swift
static func allGather(_ x: MLXArray, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

## Parameters

- `x`: Input array
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/allgather(_:group:stream:))*