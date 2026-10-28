---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.elu.html
---

# mlx.nn.elu

```python
class elu(x, alpha=1.0)
```

Applies the Exponential Linear Unit.

Simply `mx.where(x > 0, x, alpha * (mx.exp(x) - 1))`.
