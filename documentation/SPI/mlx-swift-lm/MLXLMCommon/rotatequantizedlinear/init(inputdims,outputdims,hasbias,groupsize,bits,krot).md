---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatequantizedlinear/init(inputdims:outputdims:hasbias:groupsize:bits:krot:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(inputDims:outputDims:hasBias:groupSize:bits:krot:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(inputDims: Int, outputDims: Int, hasBias: Bool, groupSize: Int, bits: Int, krot: Int)
```

## Discussion

> **Precondition**: `inputDims` is a positive multiple of an even `groupSize`, and `krot >= 1` — see `rotationGeometryProblem`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatequantizedlinear/init(inputdims:outputdims:hasbias:groupsize:bits:krot:))*