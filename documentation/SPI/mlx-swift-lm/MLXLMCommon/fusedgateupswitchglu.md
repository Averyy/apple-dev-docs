---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/fusedgateupswitchglu"
framework: "mlx-swift-lm/MLXLMCommon"
---

# FusedGateUpSwitchGLU

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

SwitchGLU variant for models that ship a single fused `gate_up_proj` weight of shape `[numExperts, 2*hiddenDims, inputDims]` instead of separate `gate_proj` / `up_proj`. Used by Gemma 4 26B MoE.

## Declaration

```swift
class FusedGateUpSwitchGLU
```

## Topics

### Initializers
- [init(inputDims: Int, hiddenDims: Int, numExperts: Int, activation: (MLXArray) -> MLXArray, bias: Bool)](./fusedgateupswitchglu/init%28inputdims,hiddendims,numexperts,activation,bias%29.md)
- [init(inputDims: Int, hiddenDims: Int, numExperts: Int, bias: Bool)](./fusedgateupswitchglu/init%28inputdims,hiddendims,numexperts,bias%29.md)
### Instance Methods
- [func callAsFunction(MLXArray, MLXArray) -> MLXArray](./fusedgateupswitchglu/callasfunction%28_,_%29.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/fusedgateupswitchglu)*