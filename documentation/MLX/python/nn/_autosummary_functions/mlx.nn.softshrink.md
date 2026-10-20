---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.softshrink.html
---

# mlx.nn.softshrink

**class softshrink(*x*, *lambd: float = 0.5*)**
: Applies the Softshrink activation function.

\[\begin{split}\text{softshrink}(x) = \begin{cases}
x - \lambda & \text{if } x > \lambda \\
x + \lambda & \text{if } x < -\lambda \\
0 & \text{otherwise}
\end{cases}\end{split}\]
