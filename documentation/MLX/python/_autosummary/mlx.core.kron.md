---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.kron.html
---

# mlx.core.kron

**

- [.rst](../../_sources/python/_autosummary/mlx.core.kron.rst)
- **

.pdf

**

# mlx.core.kron

 Table of contents 

## Contents

# mlx.core.kron

**kron(*a: array*, *b: array*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the Kronecker product of two arrays `a` and `b`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The first input array.
**b** ([array](mlx.core.array.html#mlx.core.array)) – The second input array.
**stream** (*Union**[**None**, *[Stream](stream_class.html#mlx.core.Stream)*, *[Device](mlx.core.Device.html#mlx.core.Device)*]**, **optional*) – Optional stream or
device for execution. Default: `None`.

Returns:
The Kronecker product of `a` and `b`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Examples
>>> a = mx.array([[1, 2], [3, 4]])
>>> b = mx.array([[0, 5], [6, 7]])
>>> result = mx.kron(a, b)
>>> print(result)
array([[0, 5, 0, 10],
       [6, 7, 12, 14],
       [0, 15, 0, 20],
       [18, 21, 24, 28]], dtype=int32)

** Contents
