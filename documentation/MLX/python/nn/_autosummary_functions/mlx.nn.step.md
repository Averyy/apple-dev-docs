---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.step.html
---

# mlx.nn.step

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.step.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.step

 Table of contents 

## Contents

# mlx.nn.step

**class step(*x: array*, *threshold: float = 0.0*)**
: Applies the Step Activation Function.
This function implements a binary step activation, where the output is set
to 1 if the input is greater than a specified threshold, and 0 otherwise.

\[\begin{split}\text{step}(x) = \begin{cases}
0 & \text{if } x < \text{threshold} \\
1 & \text{if } x \geq \text{threshold}
\end{cases}\end{split}\]

Parameters:
**threshold** – The value to threshold at.

** Contents
