---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.cross_entropy.html
---

# mlx.core.fast.cross_entropy

```python
cross_entropy(logits: array, targets: array, *, stream: StreamOrDevice = None) → array
```

Cross entropy loss with class indices as targets.

Computes `logsumexp(logits, axis=-1) - logits[..., target]` in a
fused kernel with accumulation in float32.

Note: The fused kernel is available on Metal and CUDA. The CPU falls
back to the unfused version, which reduces in the dtype of the logits.

**Parameters:**

- **logits** ([array](mlx.core.array.md#mlx.core.array)) – The unnormalized logits. The loss is computed over
the last axis.
- **targets** ([array](mlx.core.array.md#mlx.core.array)) – Class indices. The shape should match the shape of
`logits` with the last axis removed. The indices must be in
`[0, logits.shape[-1])`.

**Returns:**
: The per-element loss in float32, with the shape of
`targets`.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
