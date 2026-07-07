---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/init.html
---

# Initializers

**

- [.rst](../../_sources/python/nn/init.rst)
- **

.pdf

**

**
**
**

**

# Initializers

 Table of contents 

# Initializers

The `mlx.nn.init` package contains commonly used initializers for neural
network parameters. Initializers return a function which can be applied to any
input [mlx.core.array](../_autosummary/mlx.core.array.html#mlx.core.array) to produce an initialized output.

For example:

```
import mlx.core as mx
import mlx.nn as nn

init_fn = nn.init.uniform()

# Produces a [2, 2] uniform matrix
param = init_fn(mx.zeros((2, 2)))
```

To re-initialize all the parameter in an [mlx.nn.Module](module.html#mlx.nn.Module) from say a uniform
distribution, you can do:

```
import mlx.nn as nn
model = nn.Sequential(nn.Linear(5, 10), nn.ReLU(), nn.Linear(10, 5))
init_fn = nn.init.uniform(low=-0.1, high=0.1)
model.apply(init_fn)
```

| constant(value[, dtype]) | An initializer that returns an array filled withvalue. |
| --- | --- |
| normal([mean, std, dtype]) | An initializer that returns samples from a normal distribution. |
| uniform([low, high, dtype]) | An initializer that returns samples from a uniform distribution. |
| identity([dtype]) | An initializer that returns an identity matrix. |
| glorot_normal([dtype]) | A Glorot normal initializer. |
| glorot_uniform([dtype]) | A Glorot uniform initializer. |
| he_normal([dtype]) | Build a He normal initializer. |
| he_uniform([dtype]) | A He uniform (Kaiming uniform) initializer. |
| sparse(sparsity[, mean, std, dtype]) | An initializer that returns a sparse matrix. |
| orthogonal([gain, dtype]) | An initializer that returns an orthogonal matrix. |
