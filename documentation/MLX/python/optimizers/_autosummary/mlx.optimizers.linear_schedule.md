---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.linear_schedule.html
---

# mlx.optimizers.linear_schedule

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.linear_schedule.rst)
- **

.pdf

**

# mlx.optimizers.linear_schedule

 Table of contents 

## Contents

# mlx.optimizers.linear_schedule

**linear_schedule(*init: float*, *end: float*, *steps: int*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)**
: Make a linear scheduler.

Parameters:

**init** ([float](https://docs.python.org/3/library/functions.html#float)) – Initial value.
**end** ([float](https://docs.python.org/3/library/functions.html#float)) – Final value.
**steps** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of steps to apply the schedule over. The value is
`end` for any steps beyond `steps`.

Example
>>> lr_schedule = optim.linear_schedule(0, 1e-1, 100)
>>> optimizer = optim.Adam(learning_rate=lr_schedule)
>>> optimizer.learning_rate
array(0.0, dtype=float32)
>>> for _ in range(101): optimizer.update({}, {})
...
>>> optimizer.learning_rate
array(0.1, dtype=float32)

** Contents
