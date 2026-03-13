---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.LSTM.html
---

# mlx.nn.LSTM

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.LSTM.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.LSTM

 Table of contents 

## Contents

# mlx.nn.LSTM

**class LSTM(*input_size: int*, *hidden_size: int*, *bias: bool = True*)**
: An LSTM recurrent layer.
The input has shape `NLD` or `LD` where:

`N` is the optional batch dimension
`L` is the sequence length
`D` is the input’s feature dimension

Concretely, for each element of the sequence, this layer computes:

\[\begin{split}\begin{aligned}
i_t &= \sigma (W_{xi}x_t + W_{hi}h_t + b_{i}) \\
f_t &= \sigma (W_{xf}x_t + W_{hf}h_t + b_{f}) \\
g_t &= \text{tanh} (W_{xg}x_t + W_{hg}h_t + b_{g}) \\
o_t &= \sigma (W_{xo}x_t + W_{ho}h_t + b_{o}) \\
c_{t + 1} &= f_t \odot c_t + i_t \odot g_t \\
h_{t + 1} &= o_t \text{tanh}(c_{t + 1})
\end{aligned}\end{split}\]
The hidden state \(h\) and cell state \(c\) have shape `NH`
or `H`, depending on whether the input is batched or not.
The layer returns two arrays, the hidden state and the cell state at
each time step, both of shape `NLH` or `LH`.

Parameters:

**input_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Dimension of the input, `D`.
**hidden_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Dimension of the hidden state, `H`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to use biases or not. Default: `True`.

Methods

** Contents
