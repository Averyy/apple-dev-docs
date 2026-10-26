---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/sumscatter(_:group:stream:)"
framework: "mlx-swift/MLX"
---

# sumScatter(_:group:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Sum `x` across the group and shard the result along the first axis.

## Declaration

```swift
static func sumScatter(_ x: MLXArray, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) -> MLXArray
```

#### Discussion

`x.dim(0)` must be divisible by the group size.  The result is equivalent to `allSum(x)` sliced to this process’ chunk, but is performed as a single reduce-scatter collective.

Currently implemented by the NCCL and JACCL backends only.

## Parameters

- `x`: Input array
- `group`: The group, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/sumscatter(_:group:stream:))*