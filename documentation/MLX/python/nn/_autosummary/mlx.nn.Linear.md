---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Linear.html
---

# mlx.nn.Linear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Linear.rst)
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

# mlx.nn.Linear

 Table of contents 

## Contents

# mlx.nn.Linear

**class Linear(*input_dims: int*, *output_dims: int*, *bias: bool = True*)**
: Applies an affine transformation to the input.
Concretely:

\[y = x W^\top + b\]
where \(W\) has shape `[output_dims, input_dims]` and \(b\) has shape `[output_dims]`.
The values are initialized from the uniform distribution \(\mathcal{U}(-{k}, {k})\),
where \(k = \frac{1}{\sqrt{D_i}}\) and \(D_i\) is equal to `input_dims`.

Parameters:

**input_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input features
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `False` then the layer will
not use a bias. Default is `True`.

Methods

`to_quantized`([group_size, bits, mode, ...])
Return a quantized approximation of this layer.

** Contents
