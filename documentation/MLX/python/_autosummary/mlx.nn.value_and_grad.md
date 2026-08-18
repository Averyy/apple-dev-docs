---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.value_and_grad.html
---

# mlx.nn.value_and_grad

**

- [.rst](../../_sources/python/_autosummary/mlx.nn.value_and_grad.rst)
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

# mlx.nn.value_and_grad

 Table of contents 

## Contents

# mlx.nn.value_and_grad

**value_and_grad(*model: Module*, *fn: Callable*)**
: Transform the passed function `fn` to a function that computes the
gradients of `fn` wrt the model’s trainable parameters and also its
value.

Parameters:

**model** ([Module](../nn/module.html#mlx.nn.Module)) – The model whose trainable parameters to compute
gradients for
**fn** (*Callable*) – The scalar function to compute gradients for

Returns:
A callable that returns the value of `fn` and the gradients wrt the
trainable parameters of `model`

** Contents
