---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/alltoshardedlinear/toquantized(groupsize:bits:mode:)"
framework: "mlx-swift/MLXNN"
---

# toQuantized(groupSize:bits:mode:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Quantizing keeps the layer sharded.

## Declaration

```swift
override func toQuantized(groupSize: Int, bits: Int, mode: QuantizationMode) -> Module
```

#### Discussion

Without this a quantized model built by [`quantize(model:groupSize:bits:mode:filter:apply:)`](../quantize%28model,groupsize,bits,mode,filter,apply%29.md) would hold plain [`QuantizedLinear`](../quantizedlinear.md) layers that no longer communicate.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/alltoshardedlinear/toquantized(groupsize:bits:mode:))*