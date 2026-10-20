---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/fast.html
---

# Fast

| [rms_norm](_autosummary/mlx.core.fast.rms_norm.md#mlx.core.fast.rms_norm)(x, weight, eps, *[, stream]) | Root Mean Square normalization (RMS norm). |
| --- | --- |
| [layer_norm](_autosummary/mlx.core.fast.layer_norm.md#mlx.core.fast.layer_norm)(x, weight, bias, eps, *[, stream]) | Layer normalization. |
| [cross_entropy](_autosummary/mlx.core.fast.cross_entropy.md#mlx.core.fast.cross_entropy)(logits, targets, *[, stream]) | Cross entropy loss with class indices as targets. |
| [rope](_autosummary/mlx.core.fast.rope.md#mlx.core.fast.rope)(a, dims, *, traditional, base, scale, ...) | Apply rotary positional encoding to the input. |
| [scaled_dot_product_attention](_autosummary/mlx.core.fast.scaled_dot_product_attention.md#mlx.core.fast.scaled_dot_product_attention)(q, k, v, *, scale) | A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`. |
| [metal_kernel](_autosummary/mlx.core.fast.metal_kernel.md#mlx.core.fast.metal_kernel)(name, input_names, ...[, ...]) | A jit-compiled custom Metal kernel defined from a source string. |
| [cuda_kernel](_autosummary/mlx.core.fast.cuda_kernel.md#mlx.core.fast.cuda_kernel)(name, input_names, output_names, ...) | A jit-compiled custom CUDA kernel defined from a source string. |
| [precompiled_cuda_kernel](_autosummary/mlx.core.fast.precompiled_cuda_kernel.md#mlx.core.fast.precompiled_cuda_kernel)(*, name, ...) | Run a precompiled CUDA kernel defined from PTX or cubin. |
