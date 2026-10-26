---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/send(_:to:group:stream:)"
framework: "mlx-swift/MLX"
---

# send(_:to:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Send `x` to the process with rank `dst`.

## Declaration

```swift
static func send(_ x: MLXArray, to dst: Int, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

#### Return Value

An array identical to `x` which, when evaluated, performs the send

## Parameters

- `x`: Input array
- `dst`: Rank of the destination process
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/send(_:to:group:stream:))*