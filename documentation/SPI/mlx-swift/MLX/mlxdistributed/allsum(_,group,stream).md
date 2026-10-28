---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/allsum(_:group:stream:)"
framework: "mlx-swift/MLX"
---

# allSum(_:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

All reduce sum.

## Declaration

```swift
static func allSum(_ x: MLXArray, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

## Discussion

Sum `x` across all processes in the group.

## Parameters

- `x`: Input array
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/allsum(_:group:stream:))*