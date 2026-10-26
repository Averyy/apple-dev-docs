---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/multiheadattention/createadditivecausalmask(_:dtype:)"
framework: "mlx-swift/MLXNN"
---

# createAdditiveCausalMask(_:dtype:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Type Method

Creates an attention mask for use with [`callAsFunction(_:keys:values:mask:)`](./callasfunction%28_,keys,values,mask%29.md)

## Declaration

```swift
static func createAdditiveCausalMask(_ n: Int, dtype: DType = .float32) -> MLXArray
```

## Parameters

- `n`: Number of dimensions
- `dtype`: Data type of the mask


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/multiheadattention/createadditivecausalmask(_:dtype:))*