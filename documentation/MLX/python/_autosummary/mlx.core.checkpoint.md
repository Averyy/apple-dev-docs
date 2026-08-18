---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.checkpoint.html
---

# mlx.core.checkpoint

**

- [.rst](../../_sources/python/_autosummary/mlx.core.checkpoint.rst)
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

# mlx.core.checkpoint

 Table of contents 

## Contents

# mlx.core.checkpoint

**checkpoint(*fun: Callable[P, R]*) → Callable[P, R]**
: Transform the passed callable to one that performs gradient
checkpointing with respect to the inputs of the callable.
Use this to reduce memory use for gradient computations at the expense of
increased computation.

Parameters:
**fun** (*Callable*) – The function to checkpoint.

Returns:
A callable that recomputes intermediate states during gradient
computation.

** Contents
