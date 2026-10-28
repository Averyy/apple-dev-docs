---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantize(model:filter:apply:)-3yqd1"
framework: "mlx-swift/MLXNN"
---

# quantize(model:filter:apply:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Quantize the sub-modules of a module according to a filter.

## Declaration

```swift
func quantize(model: Module, filter: (String, Module) -> (groupSize: Int, bits: Int, mode: QuantizationMode)?, apply: (Module, Int, Int, QuantizationMode) -> Module? = quantizeSingle(
        layer:groupSize:bits:mode:))
```

## Discussion

By default all [`Linear`](./linear.md) and [`Embedding`](./embedding.md) layers will be quantized.

### See Also

- [`quantize(model:groupSize:bits:filter:apply:)`](./quantize%28model,groupsize,bits,filter,apply%29.md)

## Parameters

- `model`: Model to quantize
- `filter`: Filter receiving path and module – return a tuple of `(groupSize: Int, bits: Int, mode: QuantizationMode)` or `nil` to skip quantization
- `apply`: Function to attempt the quantization – the default implementation will quantize [`Linear`](./linear.md) and [`Embedding`](./embedding.md) layers


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantize(model:filter:apply:)-3yqd1)*