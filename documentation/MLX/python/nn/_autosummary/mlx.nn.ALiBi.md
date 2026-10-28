---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.ALiBi.html
---

# mlx.nn.ALiBi

```python
class ALiBi
```

Implements Attention with Linear Biases (ALiBi).

ALiBi adds a static, non-learnable bias matrix to attention scores proportional
to the distance between query and key tokens.

For more details see [Train Short, Test Long: Attention with Linear Biases Enables
Input Length Extrapolation](https://arxiv.org/abs/2108.12409).

Methods

| `create_alibi_matrix`(q_sequence_length, ...) | Create the ALiBi bias matrix. |
| --- | --- |
| `create_alibi_slope`(num_heads[, dtype]) | Create the geometric slopes for ALiBi across attention heads. |
