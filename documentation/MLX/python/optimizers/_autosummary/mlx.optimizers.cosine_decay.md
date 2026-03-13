---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.cosine_decay.html
---

# mlx.optimizers.cosine_decay

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.cosine_decay.rst)
- **

.pdf

**

**
**
**

**

# mlx.optimizers.cosine_decay

 Table of contents 

## Contents

# mlx.optimizers.cosine_decay

**cosine_decay(*init: float*, *decay_steps: int*, *end: float = 0.0*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)**
: Make a cosine decay scheduler.

Parameters:

**init** ([float](https://docs.python.org/3/library/functions.html#float)) – Initial value.
**decay_steps** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of steps to decay over. The decayed
value is constant for steps beyond `decay_steps`.
**end** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Final value to decay to. Default: `0`.

Example
>>> lr_schedule = optim.cosine_decay(1e-1, 1000)
>>> optimizer = optim.SGD(learning_rate=lr_schedule)
>>> optimizer.learning_rate
array(0.1, dtype=float32)
>>>
>>> for _ in range(5): optimizer.update({}, {})
...
>>> optimizer.learning_rate
array(0.0999961, dtype=float32)

** Contents
