---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/cpp/fast.html
---

# Fast

```cpp
array mlx::core::fast::rms_norm(const array &x, const std::optional<array> &weight, float eps, StreamOrDevice s)
```

Fused root-mean-square normalization.

```cpp
array mlx::core::fast::layer_norm(const array &x, const std::optional<array> &weight, const std::optional<array> &bias, float eps, StreamOrDevice s)
```

Fused layer normalization.

```cpp
array mlx::core::fast::cross_entropy(const array &logits, const array &targets, StreamOrDevice s)
```

Fused cross entropy with class indices as targets.

```cpp
array mlx::core::fast::rope(const array &x, int dims, bool traditional, std::optional<float> base, float scale, int offset, const std::optional<array> &freqs, StreamOrDevice s)
```

Applies rotary position embeddings with a scalar offset.

```cpp
array mlx::core::fast::rope(const array &x, int dims, bool traditional, std::optional<float> base, float scale, const array &offset, const std::optional<array> &freqs, StreamOrDevice s)
```

Applies rotary position embeddings with per-token offsets.

```cpp
array mlx::core::fast::scaled_dot_product_attention(const array &queries, const array &keys, const array &values, const float scale, int window_size, const std::string &mask_mode, std::optional<array> mask_arr, const std::optional<array> &sinks, bool force_fused, StreamOrDevice s)
```

Computes: O = softmax(Q @ K.T) @ V *

```cpp
std::vector<array> mlx::core::fast::gated_delta_update(const array &queries, const array &keys, const array &values, const array &gates, const array &beta_, const std::optional<array> &initial_state, const std::optional<array> &mask, StreamOrDevice s)
```

Updates recurrent state with the gated delta rule.

```cpp
CustomKernelFunction mlx::core::fast::metal_kernel(const std::string &name, const std::vector<std::string> &input_names, const std::vector<std::string> &output_names, const std::string &source, const std::string &header, bool ensure_row_contiguous, bool atomic_outputs, const CompileOptions &compile_options)
```

Creates a callable for a custom Metal kernel.

```cpp
CustomKernelFunction mlx::core::fast::cuda_kernel(const std::string &name, const std::vector<std::string> &input_names, const std::vector<std::string> &output_names, const std::string &source, const std::string &header, bool ensure_row_contiguous, int shared_memory)
```

Creates a callable for a custom CUDA kernel.

```cpp
std::vector<array> mlx::core::fast::precompiled_cuda_kernel(const std::string &name, const std::string &compiled_source, const std::vector<array> &inputs, const std::vector<Shape> &output_shapes, const std::vector<Dtype> &output_dtypes, const std::vector<ScalarArg> &scalars, std::tuple<int, int, int> grid, std::tuple<int, int, int> threadgroup, int shared_memory, std::optional<float> init_value, bool ensure_row_contiguous, StreamOrDevice s)
```

Runs a precompiled CUDA kernel with the given inputs and launch parameters.
