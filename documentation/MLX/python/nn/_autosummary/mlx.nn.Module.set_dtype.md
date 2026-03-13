---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.set_dtype.html
---

# mlx.nn.Module.set_dtype

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.set_dtype.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.Module.set_dtype

 Table of contents 

## Contents

# mlx.nn.Module.set_dtype

**Module.set_dtype(*dtype: ~mlx.core.Dtype, predicate: ~typing.Callable[[~mlx.core.Dtype], bool] | None = <function Module.<lambda>>*)**
: Set the dtype of the module’s parameters.

Parameters:

**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)) – The new dtype.
**predicate** ([Callable](https://docs.python.org/3/library/typing.html#typing.Callable)*, **optional*) – A predicate to select
parameters to cast. By default, only parameters of type
`floating` will be updated to avoid casting integer
parameters to the new dtype.

** Contents
