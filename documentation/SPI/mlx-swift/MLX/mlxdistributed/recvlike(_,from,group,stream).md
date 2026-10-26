---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/recvlike(_:from:group:stream:)"
framework: "mlx-swift/MLX"
---

# recvLike(_:from:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Receive an array with the same shape and type as `x` from the process with rank `src`.

## Declaration

```swift
static func recvLike(_ x: MLXArray, from src: Int, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

## Parameters

- `x`: Array whose shape and type describe what will be received
- `src`: Rank of the source process
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/recvlike(_:from:group:stream:))*