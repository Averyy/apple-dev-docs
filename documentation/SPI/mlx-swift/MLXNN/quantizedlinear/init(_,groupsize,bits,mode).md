---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/init(_:groupsize:bits:mode:)"
framework: "mlx-swift/MLXNN"
---

# init(_:groupSize:bits:mode:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Initialize a QuantizedLinear layer that applies the same linear transformation up to the quantization error.

## Declaration

```swift
convenience init(_ other: Linear, groupSize: Int = 64, bits: Int = 4, mode: QuantizationMode = .affine)
```

## Parameters

- `other`: A `Linear` layer
- `groupSize`: The group size to use for the quantized weight
- `bits`: The bit width to use for the quantized weight
- `mode`: Quantization mode


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/init(_:groupsize:bits:mode:))*