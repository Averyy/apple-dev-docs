---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.optimizers.clip_grad_norm.html
---

# mlx.optimizers.clip_grad_norm

**

- [.rst](../../_sources/python/_autosummary/mlx.optimizers.clip_grad_norm.rst)
- **

.pdf

**

# mlx.optimizers.clip_grad_norm

 Table of contents 

## Contents

# mlx.optimizers.clip_grad_norm

**clip_grad_norm(*grads*, *max_norm*)**
: Clips the global norm of the gradients.
This function ensures that the global norm of the gradients does not exceed
`max_norm`. It scales down the gradients proportionally if their norm is
greater than `max_norm`.
Example
>>> grads = {"w1": mx.array([2, 3]), "w2": mx.array([1])}
>>> clipped_grads, total_norm = clip_grad_norm(grads, max_norm=2.0)
>>> print(clipped_grads)
{"w1": mx.array([...]), "w2": mx.array([...])}

Parameters:

**grads** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – A dictionary containing the gradient arrays.
**max_norm** ([float](https://docs.python.org/3/library/functions.html#float)) – The maximum allowed global norm of the gradients.

Returns:
The possibly rescaled gradients and the original
gradient norm.

Return type:
([dict](https://docs.python.org/3/library/stdtypes.html#dict), [float](https://docs.python.org/3/library/functions.html#float))

** Contents
