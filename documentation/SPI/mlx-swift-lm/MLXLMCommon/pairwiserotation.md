---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/pairwiserotation"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PairwiseRotation

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Standalone pairwise Givens rotation over the last axis of an activation tensor, fused with per-channel scaling in a single Metal kernel.

## Declaration

```swift
class PairwiseRotation
```

#### Overview

This is the rotation half of `RotateQuantizedLinear`, extracted as a composable `Module` for layers whose rotation is *shared* across several quantized projections instead of owned by one — the MoE `RotateSwitchGLU` composes two of these (`gate_up_rot`, `down_rot`) around stock `QuantizedSwitchLinear` experts.

Checkpoint contract: `theta` / `pairs` / `channel_scales` load via Module reflection under this module’s key prefix (e.g. `switch_mlp.gate_up_rot.theta`). After loading, the owner must call `prepareDerivedRotationState()` once, before any forward pass.

## Topics

### Initializers
- [init(dims: Int, groupSize: Int, krot: Int)](./pairwiserotation/init%28dims,groupsize,krot%29.md)
### Instance Methods
- [func prepareDerivedRotationState() -> [MLXArray]](./pairwiserotation/preparederivedrotationstate%28%29.md)
  See `RotationStatePreparing` — loader-owned, results batched into a single load-time `eval` with every other rotation module’s.
- [func rotate(MLXArray) -> MLXArray](./pairwiserotation/rotate%28_%29.md)
  Apply channel scaling + pairwise Givens rotations to the last axis.

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/pairwiserotation)*