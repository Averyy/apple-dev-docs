---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/allmax(_:group:stream:)"
framework: "mlx-swift/MLX"
---

# allMax(_:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

All reduce max.

## Declaration

```swift
static func allMax(_ x: MLXArray, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

## Parameters

- `x`: Input array
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/allmax(_:group:stream:))*