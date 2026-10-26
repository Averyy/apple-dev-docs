---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/init(weight:bias:scales:biases:groupsize:bits:mode:globalscale:)"
framework: "mlx-swift/MLXNN"
---

# init(weight:bias:scales:biases:groupSize:bits:mode:globalScale:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Initializer meant for subclasses to provide arrays directly.

## Declaration

```swift
init(weight: MLXArray, bias: MLXArray? = nil, scales: MLXArray, biases: MLXArray?, groupSize: Int, bits: Int, mode: QuantizationMode = .affine, globalScale: MLXArray? = nil)
```

##### See Also

- [`init(weight:bias:)`](../linear/init%28weight,bias%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/init(weight:bias:scales:biases:groupsize:bits:mode:globalscale:))*