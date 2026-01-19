---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.exponential_decay.html
---

# mlx.optimizers.exponential_decay

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.exponential_decay.rst)
- **

.pdf

**

# mlx.optimizers.exponential_decay

 Table of contents 

## Contents

# mlx.optimizers.exponential_decay

**exponential_decay(*init: float*, *decay_rate: float*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)**
: Make an exponential decay scheduler.

Parameters:

**init** ([float](https://docs.python.org/3/library/functions.html#float)) – Initial value.
**decay_rate** ([float](https://docs.python.org/3/library/functions.html#float)) – Multiplicative factor to decay by.

Example
>>> lr_schedule = optim.exponential_decay(1e-1, 0.9)
>>> optimizer = optim.SGD(learning_rate=lr_schedule)
>>> optimizer.learning_rate
array(0.1, dtype=float32)
>>>
>>> for _ in range(5): optimizer.update({}, {})
...
>>> optimizer.learning_rate
array(0.06561, dtype=float32)

** Contents
