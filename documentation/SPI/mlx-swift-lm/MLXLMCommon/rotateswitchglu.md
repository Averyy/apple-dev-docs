---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotateswitchglu"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RotateSwitchGLU

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

`SwitchGLU` with shared pairwise Givens rotations injected around the expert projections — the PARO MoE expert block (mirrors upstream z-lab `RotateSwitchGLU`, paroquant `modules.py`).

## Declaration

```swift
class RotateSwitchGLU
```

## Overview

All experts share a single set of rotation parameters per projection input: `gate_up_rot` rotates the token activations ahead of the expert gather (bitwise-equivalent to rotating the gathered rows, at 1/topK the cost) for `gate_proj`/`up_proj` (which share their input), and `down_rot` rotates the activated hidden state before `down_proj`. The projections themselves stay stock `SwitchLinear`/`QuantizedSwitchLinear` — rotating the shared activations *once* per token is what makes PARO MoE cheap: the rotation cost is independent of the number of experts.

Checkpoint contract: the rotation parameters load under *nested* keys (`switch_mlp.gate_up_rot.theta`, `switch_mlp.down_rot.pairs`, …) via the two `PairwiseRotation` children. Upstream keeps them flat on the GLU (`gate_up_rot_theta`); the nested layout is a deliberate divergence (#208) so the rotation is a reusable Module rather than mixin state — `remapSharedMoERotations` in the loader produces the nested keys.

Subclasses `SwitchGLU` so it satisfies the `switch_mlp: SwitchGLU` property on MoE blocks (e.g. `Qwen35SparseMoeBlock`) through `update(modules:)`, exactly like `RotateQuantizedLinear: QuantizedLinear` on the dense path.

## Topics

### Initializers
- [init(inputDims: Int, hiddenDims: Int, numExperts: Int, groupSize: Int, krot: Int, bias: Bool)](./rotateswitchglu/init%28inputdims,hiddendims,numexperts,groupsize,krot,bias%29.md)

## Relationships

### Inherits From
- [SwitchGLU](./switchglu.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotateswitchglu)*