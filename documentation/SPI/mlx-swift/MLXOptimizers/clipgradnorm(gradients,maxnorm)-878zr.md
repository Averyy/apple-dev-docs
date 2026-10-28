---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/clipgradnorm(gradients:maxnorm:)-878zr"
framework: "mlx-swift/MLXOptimizers"
---

# clipGradNorm(gradients:maxNorm:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: func  
**Role**: Function

Clips the global norm of the gradients.

## Declaration

```swift
func clipGradNorm(gradients: some Collection<MLXArray>, maxNorm: Float) -> ([MLXArray], MLXArray)
```

## Discussion

This function ensures that the global norm of the gradients does not exceed `max_norm`. It scales down the gradients proportionally if their norm is greater than `max_norm`.

## Parameters

- `gradients`: An array of MLXArray
- `maxNorm`: The maximum allowed global norm of th gradients


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/clipgradnorm(gradients:maxnorm:)-878zr)*