---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GELU.html
---

# mlx.nn.GELU

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.GELU.rst)
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

# mlx.nn.GELU

 Table of contents 

## Contents

# mlx.nn.GELU

**class GELU(*approx='none'*)**
: Applies the Gaussian Error Linear Units.

\[\textrm{GELU}(x) = x * \Phi(x)\]
where \(\Phi(x)\) is the Gaussian CDF.
However, if `approx` is set to ‘precise’ or ‘fast’ it applies

\[\begin{split}\textrm{GELUApprox}(x) &= 0.5 * x * \left(1 + \text{Tanh}\left(\sqrt{2 / \pi} * \left(x + 0.044715 * x^3\right)\right)\right) \\
\textrm{GELUFast}(x) &= x * \sigma\left(1.702 * x\right)\end{split}\]
respectively.

Note
For compatibility with the PyTorch API, ‘tanh’ can be used as an alias
for ‘precise’.

See [gelu()](../_autosummary_functions/mlx.nn.gelu.html#mlx.nn.gelu), [gelu_approx()](../_autosummary_functions/mlx.nn.gelu_approx.html#mlx.nn.gelu_approx) and [gelu_fast_approx()](../_autosummary_functions/mlx.nn.gelu_fast_approx.html#mlx.nn.gelu_fast_approx) for the
functional equivalents and information regarding error bounds.

Parameters:
**approx** (*'none'** | **'precise'** | **'fast'*) – Which approximation to gelu to use if any.

Methods

** Contents
