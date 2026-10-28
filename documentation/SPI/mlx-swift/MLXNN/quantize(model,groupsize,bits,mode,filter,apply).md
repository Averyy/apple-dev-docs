---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantize(model:groupsize:bits:mode:filter:apply:)"
framework: "mlx-swift/MLXNN"
---

# quantize(model:groupSize:bits:mode:filter:apply:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Quantize the sub-modules of a module according to a filter.

## Declaration

```swift
func quantize(model: Module, groupSize: Int = 64, bits: Int = 4, mode: QuantizationMode = .affine, filter: (String, Module) -> Bool = { _, _ in true }, apply: (Module, Int, Int, QuantizationMode) -> Module? = quantizeSingle(
        layer:groupSize:bits:mode:))
```

## Discussion

By default all [`Linear`](./linear.md) and [`Embedding`](./embedding.md) layers will be quantized.

### See Also

- [`quantize(model:filter:apply:)`](./quantize%28model,filter,apply%29-3yqd1.md)

## Parameters

- `model`: Model to quantize
- `groupSize`: Quantization group size
- `bits`: Bits per parameter
- `mode`: Quantization mode
- `filter`: Filter receiving path and module – return `false` to skip a layer
- `apply`: Function to attempt the quantization – the default implementation will quantize [`Linear`](./linear.md) and [`Embedding`](./embedding.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantize(model:groupsize:bits:mode:filter:apply:))*