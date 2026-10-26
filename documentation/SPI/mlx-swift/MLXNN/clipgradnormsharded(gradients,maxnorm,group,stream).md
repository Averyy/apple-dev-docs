---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/clipgradnormsharded(gradients:maxnorm:group:stream:)"
framework: "mlx-swift/MLXNN"
---

# clipGradNormSharded(gradients:maxNorm:group:stream:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Clip the global norm of gradients that are sharded across a group.

## Declaration

```swift
func clipGradNormSharded(gradients: ModuleParameters, maxNorm: Float, group: MLXDistributed.Group? = nil, stream: StreamOrDevice = .cpu) throws -> (ModuleParameters, MLXArray)
```

#### Return Value

The rescaled shard and the global gradient norm

#### Discussion

This is the sharded counterpart of `clipGradNorm` in MLXOptimizers: no process holds the whole gradient, so the local squared norms are summed across the group before anything is rescaled.

## Parameters

- `gradients`: This process’ shard of the gradients
- `maxNorm`: The maximum allowed global norm
- `group`: The group the gradients are sharded across, or `nil` to use the global group
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/clipgradnormsharded(gradients:maxnorm:group:stream:))*