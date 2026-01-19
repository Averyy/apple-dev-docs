---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GRU.html
---

# mlx.nn.GRU

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.GRU.rst)
- **

.pdf

**

# mlx.nn.GRU

 Table of contents 

## Contents

# mlx.nn.GRU

**class GRU(*input_size: int*, *hidden_size: int*, *bias: bool = True*)**
: A gated recurrent unit (GRU) RNN layer.
The input has shape `NLD` or `LD` where:

`N` is the optional batch dimension
`L` is the sequence length
`D` is the input’s feature dimension

Concretely, for each element of the sequence, this layer computes:

\[\begin{split}\begin{aligned}
r_t &= \sigma (W_{xr}x_t + W_{hr}h_t + b_{r}) \\
z_t &= \sigma (W_{xz}x_t + W_{hz}h_t + b_{z}) \\
n_t &= \text{tanh}(W_{xn}x_t + b_{n} + r_t \odot (W_{hn}h_t + b_{hn})) \\
h_{t + 1} &= (1 - z_t) \odot n_t + z_t \odot h_t
\end{aligned}\end{split}\]
The hidden state \(h\) has shape `NH` or `H` depending on
whether the input is batched or not. Returns the hidden state at each
time step of shape `NLH` or `LH`.

Parameters:

**input_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Dimension of the input, `D`.
**hidden_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Dimension of the hidden state, `H`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to use biases or not. Default: `True`.

Methods

** Contents
