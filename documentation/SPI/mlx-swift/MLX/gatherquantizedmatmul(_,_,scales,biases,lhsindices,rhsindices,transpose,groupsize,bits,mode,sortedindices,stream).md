---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gatherquantizedmatmul(_:_:scales:biases:lhsindices:rhsindices:transpose:groupsize:bits:mode:sortedindices:stream:)"
framework: "mlx-swift/MLX"
---

# gatherQuantizedMatmul(_:_:scales:biases:lhsIndices:rhsIndices:transpose:groupSize:bits:mode:sortedIndices:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func gatherQuantizedMatmul(_ x: MLXArray, _ w: MLXArray, scales: MLXArray, biases: MLXArray?, lhsIndices: MLXArray? = nil, rhsIndices: MLXArray? = nil, transpose: Bool = true, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .affine, sortedIndices: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gatherquantizedmatmul(_:_:scales:biases:lhsindices:rhsindices:transpose:groupsize:bits:mode:sortedindices:stream:))*