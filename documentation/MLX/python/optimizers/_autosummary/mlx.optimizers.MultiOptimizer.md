---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.MultiOptimizer.html
---

# mlx.optimizers.MultiOptimizer

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.MultiOptimizer.rst)
- **

.pdf

**

**
**
**

**

# mlx.optimizers.MultiOptimizer

 Table of contents 

## Contents

# mlx.optimizers.MultiOptimizer

**class MultiOptimizer(*optimizers*, *filters: list = []*)**
: Wraps a list of optimizers with corresponding weight predicates/filters
to make it easy to use different optimizers for different weights.
The predicates take the full “path” of the weight and the weight itself and
return True if it should be considered for this optimizer. The last
optimizer in the list is a fallback optimizer and no predicate should be
given for it.

Parameters:

**optimizers** ([list](https://docs.python.org/3/library/stdtypes.html#list)*[*[Optimizer](../optimizer.html#mlx.optimizers.Optimizer)*]*) – A list of optimizers to delegate to
**filters** ([list](https://docs.python.org/3/library/stdtypes.html#list)*[**Callable**[**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[array](../../_autosummary/mlx.core.array.html#mlx.core.array)*]**, *[bool](https://docs.python.org/3/library/functions.html#bool)*]*) – A list of predicates that
should be one less than the provided optimizers.

Methods

`__init__`(optimizers[, filters])

`apply_gradients`(gradients, parameters)
Apply the gradients to the parameters and return the updated parameters.

`init`(parameters)
Initialize the optimizer's state

** Contents
