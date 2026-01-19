---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array.at.html
---

# mlx.core.array.at

**

- [.rst](../../_sources/python/_autosummary/mlx.core.array.at.rst)
- **

.pdf

**

# mlx.core.array.at

 Table of contents 

## Contents

# mlx.core.array.at

**property array.at**
: Used to apply updates at the given indices.

Note
Regular in-place updates map to assignment. For instance `x[idx] += y`
maps to `x[idx] = x[idx] + y`. As a result, assigning to the
same index ignores all but one update. Using `x.at[idx].add(y)`
will correctly apply all updates to all indices.

array.at syntax
In-place syntax

`x = x.at[idx].add(y)`
`x[idx] += y`

`x = x.at[idx].subtract(y)`
`x[idx] -= y`

`x = x.at[idx].multiply(y)`
`x[idx] *= y`

`x = x.at[idx].divide(y)`
`x[idx] /= y`

`x = x.at[idx].maximum(y)`
`x[idx] = mx.maximum(x[idx], y)`

`x = x.at[idx].minimum(y)`
`x[idx] = mx.minimum(x[idx], y)`

Example
>>> a = mx.array([0, 0])
>>> idx = mx.array([0, 1, 0, 1])
>>> a[idx] += 1
>>> a
array([1, 1], dtype=int32)
>>>
>>> a = mx.array([0, 0])
>>> a.at[idx].add(1)
array([2, 2], dtype=int32)

** Contents
