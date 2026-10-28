---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/averagegradients(_:group:allreducesize:stream:)"
framework: "mlx-swift/MLXNN"
---

# averageGradients(_:group:allReduceSize:stream:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Average the gradients across the processes in the group.

## Declaration

```swift
func averageGradients(_ gradients: ModuleParameters, group: MLXDistributed.Group? = nil, allReduceSize: Int = 32 * 1024 * 1024, stream: StreamOrDevice = .cpu) throws -> ModuleParameters
```

## Discussion

Small gradients are concatenated into batches of at least `allReduceSize` bytes so that they are communicated in one step, which is considerably faster than one call per array.

## Parameters

- `gradients`: The gradients, which must have the same structure in every process
- `group`: The group to average across, or `nil` to use the global group
- `allReduceSize`: Group arrays until their size in bytes exceeds this, or `0` to disable grouping
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/averagegradients(_:group:allreducesize:stream:))*