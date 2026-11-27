---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.gated_delta_update.html
---

# mlx.core.fast.gated_delta_update

```python
gated_delta_update(q: array, k: array, v: array, gamma: array, beta: array, initial_state: array | None = None, mask: array | None = None, stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None) → list[array]
```

Gated delta network forward pass.

The number of value heads `Hv` must be a multiple of the number
of query and key heads `Hk`.

**Parameters:**

- **q** ([array](mlx.core.array.md#mlx.core.array)) – Queries with shape `[B, T, Hk, Dk]`.
- **k** ([array](mlx.core.array.md#mlx.core.array)) – Keys with shape `[B, T, Hk, Dk]`.
- **v** ([array](mlx.core.array.md#mlx.core.array)) – Values with shape `[B, T, Hv, Dv]`.
- **gamma** ([array](mlx.core.array.md#mlx.core.array)) – Decay rates in linear space with shape
`[B, T, Hv]` or `[B, T, Hv, Dk]`.
- **beta** ([array](mlx.core.array.md#mlx.core.array)) – Delta update rates with shape `[B, T, Hv]`.
- **initial_state** ([array](mlx.core.array.md#mlx.core.array), *optional*) – Initial state with shape
`[B, Hv, Dv, Dk]`. Default: zeros.
- **mask** ([array](mlx.core.array.md#mlx.core.array), *optional*) – Boolean mask with shape `[B, T]`.
False entries leave the state unchanged and produce zero
output. Default: `None`.

**Returns:**
: The output with shape `[B, T, Hv, Dv]` and the
final state with shape `[B, Hv, Dv, Dk]` and dtype `float32`.

**Return type:**
: [list](https://docs.python.org/3/builtins/stdtypes.html#list)([array](mlx.core.array.md#mlx.core.array))
