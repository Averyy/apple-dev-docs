---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/from(linear:groupsize:bits:)"
framework: "mlx-swift/MLXNN"
---

# from(linear:groupSize:bits:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Type Method

Returns a QuantizedLinear layer that applies the same linear transformation up to the quantization error.

## Declaration

```swift
static func from(linear: Linear, groupSize: Int = 64, bits: Int = 4) -> QuantizedLinear
```

## Return Value

A new `QuantizedLayer`

## Parameters

- `linear`: A `Linear` layer
- `groupSize`: The group size to use for the quantized weight
- `bits`: The bit width to use for the quantized weight


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/from(linear:groupsize:bits:))*