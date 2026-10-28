---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rope/callasfunction(_:offset:)-1d45j"
framework: "mlx-swift/MLXNN"
---

# callAsFunction(_:offset:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Evaluate with array offset for batched inference with different positions per sequence.

## Declaration

```swift
func callAsFunction(_ x: MLXArray, offset: MLXArray) -> MLXArray
```

## Return Value

The input with rotary positional encoding applied

## Parameters

- `x`: Input array
- `offset`: Integer position offsets (recommended `.int32`) as a scalar or a vector of length `batchSize`. For no offset, call [`callAsFunction(_:)`](./callasfunction%28_%29.md) or pass `MLXArray([Int32(0)])`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rope/callasfunction(_:offset:)-1d45j)*