---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.ELU.html
---

# mlx.nn.ELU

```python
class ELU(alpha=1.0)
```

**Applies the Exponential Linear Unit.**
: Simply `mx.where(x > 0, x, alpha * (mx.exp(x) - 1))`.

See [elu()](../_autosummary_functions/mlx.nn.elu.md#mlx.nn.elu) for the functional equivalent.

**Parameters:**
: **alpha** – the \(\alpha\) value for the ELU formulation. Default: `1.0`

Methods
