---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/quantize(model:groupsize:bits:predicate:)"
framework: "mlx-swift/MLXNN"
---

# quantize(model:groupSize:bits:predicate:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Type Method

Replace [`Linear`](../linear.md) layers with `QuantizedLinear`.

## Declaration

```swift
static func quantize(model: Module, groupSize: Int = 64, bits: Int = 4, predicate: (Linear) -> Bool = { _ in true })
```

## Mentions

- [Creating Modules](../custom-layers.md)

## Discussion

Please see the discussion in [`Linear`](../linear.md) for considerations when replacing layers.

## Parameters

- `model`: The model to update
- `groupSize`: The group size to use for the quantized weight
- `bits`: The bit width to use for the quantized weight
- `predicate`: Optional predicate for identifying layers to change – default finds all `Linear` layers


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/quantize(model:groupsize:bits:predicate:))*