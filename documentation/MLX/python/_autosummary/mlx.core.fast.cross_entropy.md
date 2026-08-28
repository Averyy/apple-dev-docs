---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.cross_entropy.html
---

# mlx.core.fast.cross_entropy

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.cross_entropy.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.fast.cross_entropy

 Table of contents 

## Contents

# mlx.core.fast.cross_entropy

**cross_entropy(*logits: array*, *targets: array*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Cross entropy loss with class indices as targets.
Computes `logsumexp(logits, axis=-1) - logits[..., target]` in a
fused kernel with accumulation in float32.
Note: Currently is implemented only on CUDA, fallback to unfused version with
manual casting on Metal and CPU.

Parameters:

**logits** ([array](mlx.core.array.html#mlx.core.array)) – The unnormalized logits. The loss is computed over
the last axis.
**targets** ([array](mlx.core.array.html#mlx.core.array)) – Class indices. The shape should match the shape of
`logits` with the last axis removed. The indices must be in
`[0, logits.shape[-1])`.

Returns:
The per-element loss in float32, with the shape of
`targets`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
