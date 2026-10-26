---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantize(model:groupsize:bits:filter:apply:)"
framework: "mlx-swift/MLXNN"
---

# quantize(model:groupSize:bits:filter:apply:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

> **Deprecated**: use quantize that takes a 4 argument apply

## Declaration

```swift
func quantize(model: Module, groupSize: Int = 64, bits: Int = 4, filter: (String, Module) -> Bool = { _, _ in true }, apply: (Module, Int, Int) -> Module? = {
        quantizeSingle(layer: $0, groupSize: $1, bits: $2, mode: .affine)
    })
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantize(model:groupsize:bits:filter:apply:))*