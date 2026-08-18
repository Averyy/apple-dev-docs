---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Bilinear.html
---

# mlx.nn.Bilinear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Bilinear.rst)
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

# mlx.nn.Bilinear

 Table of contents 

## Contents

# mlx.nn.Bilinear

**class Bilinear(*input1_dims: int*, *input2_dims: int*, *output_dims: int*, *bias: bool = True*)**
: Applies a bilinear transformation to the inputs.
Concretely:

\[y_i = x_2^\top W_i x_1 + b_i\]
where:
\(W\) has shape `[output_dims, input2_dims, input1_dims]`, \(b\) has shape `[output_dims]`,
and \(i\) indexes the output dimension.
The values are initialized from the uniform distribution \(\mathcal{U}(-{k}, {k})\),
where \(k = \frac{1}{\sqrt{D_1}}\) and \(D_1\) is `input1_dims`.

Parameters:

**input1_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input1 features
**input2_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input2 features
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `False` then the layer will
not use a bias. Default is `True`.

Methods

** Contents
