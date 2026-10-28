---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.get_active_memory.html
---

# mlx.core.get_active_memory

```python
get_active_memory() → int
```

Get the actively used memory in bytes.

Note, this will not always match memory use reported by the system because
it does not include cached memory buffers.
