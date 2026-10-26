---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sumgradients(group:)"
framework: "mlx-swift/MLXNN"
---

# sumGradients(group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Returns a function that is the identity in the forward pass and sums the gradients across the group in the backward pass.

## Declaration

```swift
func sumGradients(group: MLXDistributed.Group) -> (MLXArray) -> MLXArray
```

## Parameters

- `group`: The group to sum across


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sumgradients(group:))*