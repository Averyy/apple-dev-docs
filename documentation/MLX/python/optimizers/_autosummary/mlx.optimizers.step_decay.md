---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.step_decay.html
---

# mlx.optimizers.step_decay

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.step_decay.rst)
- **

.pdf

**

**
**
**

**

# mlx.optimizers.step_decay

 Table of contents 

## Contents

# mlx.optimizers.step_decay

**step_decay(*init: float*, *decay_rate: float*, *step_size: int*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)**
: Make a step decay scheduler.

Parameters:

**init** ([float](https://docs.python.org/3/library/functions.html#float)) – Initial value.
**decay_rate** ([float](https://docs.python.org/3/library/functions.html#float)) – Multiplicative factor to decay by.
**step_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Decay every `step_size` steps.

Example
>>> lr_schedule = optim.step_decay(1e-1, 0.9, 10)
>>> optimizer = optim.SGD(learning_rate=lr_schedule)
>>> optimizer.learning_rate
array(0.1, dtype=float32)
>>>
>>> for _ in range(21): optimizer.update({}, {})
...
>>> optimizer.learning_rate
array(0.081, dtype=float32)

** Contents
