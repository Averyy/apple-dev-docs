---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/fast.html
---

# Fast

**

- [.rst](../_sources/python/fast.rst)
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

# Fast

 Table of contents 

# Fast

| rms_norm(x, weight, eps, *[, stream]) | Root Mean Square normalization (RMS norm). |
| --- | --- |
| layer_norm(x, weight, bias, eps, *[, stream]) | Layer normalization. |
| rope(a, dims, *, traditional, base, scale, ...) | Apply rotary positional encoding to the input. |
| scaled_dot_product_attention(q, k, v, *, scale) | A fast implementation of multi-head attention:O=softmax(Q@K.T,dim=-1)@V. |
| metal_kernel(name, input_names, ...[, ...]) | A jit-compiled custom Metal kernel defined from a source string. |
| cuda_kernel(name, input_names, output_names, ...) | A jit-compiled custom CUDA kernel defined from a source string. |
| precompiled_cuda_kernel(*, name, ...) | Run a precompiled CUDA kernel defined from PTX or cubin. |
