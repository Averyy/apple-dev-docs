---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.cuda.get_arch_list.html
---

# mlx.core.cuda.get_arch_list

```python
get_arch_list() → list[str]
```

Get the CUDA architectures MLX was compiled for.

Architectures use NVIDIA’s `sm_*` (binary) and `compute_*` (PTX)
notation, for example `["sm_80", "sm_120a", "compute_120"]`.

**Returns:**
: The compiled architectures, or an empty list if CUDA
backend is not enabled.

**Return type:**
: [list](https://docs.python.org/3/builtins/stdtypes.html#list)([str](https://docs.python.org/3/builtins/stdtypes.html#str))
