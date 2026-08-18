---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.gelu_approx.html
---

# mlx.nn.gelu_approx

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.gelu_approx.rst)
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

# mlx.nn.gelu_approx

 Table of contents 

## Contents

# mlx.nn.gelu_approx

**class gelu_approx(*x*)**
: An approximation to Gaussian Error Linear Unit.
See [gelu()](mlx.nn.gelu.html#mlx.nn.gelu) for the exact computation.
This function approximates `gelu` with a maximum absolute error \(<
0.0005\) in the range \([-6, 6]\) using the following

\[x = 0.5 * x * \left(1 + \text{Tanh}\left(\sqrt{2 / \pi} * \left(x + 0.044715 * x^3\right)\right)\right)\]

** Contents
