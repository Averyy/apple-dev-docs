---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/recv(_:dtype:from:group:stream:)"
framework: "mlx-swift/MLX"
---

# recv(_:dtype:from:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Receive an array with the given shape and type from the process with rank `src`.

## Declaration

```swift
static func recv(_ shape: [Int], dtype: DType, from src: Int, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

## Parameters

- `shape`: Shape of the array to receive
- `dtype`: Type of the array to receive
- `src`: Rank of the source process
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/recv(_:dtype:from:group:stream:))*