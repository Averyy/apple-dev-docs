---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.l1_loss.html
---

# mlx.nn.losses.l1_loss

```python
class l1_loss(predictions: array, targets: array, reduction: Literal['none', 'mean', 'sum'] = 'mean')
```

Computes the L1 loss.

**Parameters:**

- **predictions** ([array](../../_autosummary/mlx.core.array.md#mlx.core.array)) – The predicted values.
- **targets** ([array](../../_autosummary/mlx.core.array.md#mlx.core.array)) – The target values.
- **reduction** ([str](https://docs.python.org/3/builtins/stdtypes.html#str), *optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'mean'`.

**Returns:**
: The computed L1 loss.

**Return type:**
: [array](../../_autosummary/mlx.core.array.md#mlx.core.array)
