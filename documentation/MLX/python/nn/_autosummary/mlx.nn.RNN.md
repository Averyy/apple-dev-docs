---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.RNN.html
---

# mlx.nn.RNN

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.RNN.rst)
- **

.pdf

**

# mlx.nn.RNN

 Table of contents 

## Contents

# mlx.nn.RNN

**class RNN(*input_size: int*, *hidden_size: int*, *bias: bool = True*, *nonlinearity: Callable | None = None*)**
: An Elman recurrent layer.
The input is a sequence of shape `NLD` or `LD` where:

`N` is the optional batch dimension
`L` is the sequence length
`D` is the input’s feature dimension

Concretely, for each element along the sequence length axis, this
layer applies the function:

\[h_{t + 1} = \text{tanh} (W_{ih}x_t + W_{hh}h_t + b)\]
The hidden state \(h\) has shape `NH` or `H`, depending on
whether the input is batched or not. Returns the hidden state at each
time step, of shape `NLH` or `LH`.

Parameters:

**input_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Dimension of the input, `D`.
**hidden_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Dimension of the hidden state, `H`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether to use a bias. Default: `True`.
**nonlinearity** (*callable**, **optional*) – Non-linearity to use. If `None`,
then func:tanh is used. Default: `None`.

Methods

** Contents
