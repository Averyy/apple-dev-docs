---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizesingle(layer:groupsize:bits:mode:)"
framework: "mlx-swift/MLXNN"
---

# quantizeSingle(layer:groupSize:bits:mode:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Quantize any [`Quantizable`](./quantizable.md) layer that is not already quantized.

## Declaration

```swift
func quantizeSingle(layer: Module, groupSize: Int = 64, bits: Int = 4, mode: QuantizationMode = .affine) -> (any Quantized)?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizesingle(layer:groupsize:bits:mode:))*