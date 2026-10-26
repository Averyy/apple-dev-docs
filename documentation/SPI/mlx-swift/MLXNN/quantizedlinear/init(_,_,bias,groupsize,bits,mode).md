---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/init(_:_:bias:groupsize:bits:mode:)"
framework: "mlx-swift/MLXNN"
---

# init(_:_:bias:groupSize:bits:mode:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies an affine transformation to the input using a quantized weight matrix.

## Declaration

```swift
convenience init(_ inputDimensions: Int, _ outputDimensions: Int, bias: Bool = true, groupSize: Int = 64, bits: Int = 4, mode: QuantizationMode = .affine)
```

#### Discussion

This is the quantized version of [`Linear`](../linear.md).  Typically this is used via [`quantize(model:groupSize:bits:predicate:)`](./quantize%28model,groupsize,bits,predicate%29.md).

## Parameters

- `inputDimensions`: Number of input dimensions
- `outputDimensions`: Number of output dimensions
- `bias`: If `true` this layer will apply a bias
- `groupSize`: The group size to use for the quantized weight
- `bits`: The bit width to use for the quantized weight
- `mode`: Quantization mode


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/init(_:_:bias:groupsize:bits:mode:))*