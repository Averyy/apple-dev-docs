---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.gelu_fast_approx.html
---

# mlx.nn.gelu_fast_approx

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.gelu_fast_approx.rst)
- **

.pdf

**

# mlx.nn.gelu_fast_approx

 Table of contents 

## Contents

# mlx.nn.gelu_fast_approx

**class gelu_fast_approx(*x*)**
: A fast approximation to Gaussian Error Linear Unit.
See [gelu()](mlx.nn.gelu.html#mlx.nn.gelu) for the exact computation.
This function approximates `gelu` with a maximum absolute error \(<
0.015\) in the range \([-6, 6]\) using the following

\[x = x \sigma\left(1.702 x\right)\]
where \(\sigma(\cdot)\) is the logistic sigmoid.
References:
- [hendrycks/GELUs](https://github.com/hendrycks/GELUs)
- [https://arxiv.org/abs/1606.08415](https://arxiv.org/abs/1606.08415)

** Contents
