---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.join_schedules.html
---

# mlx.optimizers.join_schedules

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.join_schedules.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.optimizers.join_schedules

 Table of contents 

## Contents

# mlx.optimizers.join_schedules

**join_schedules(*schedules: List[Callable]*, *boundaries: List[int]*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)**
: Join multiple schedules to create a new schedule.

Parameters:

**schedules** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(**Callable**)*) – A list of schedules. Schedule \(i+1\)
receives a step count indicating the number of steps since
the \(i\)-th boundary.
**boundaries** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – A list of integers of length `len(schedules) - 1`
that indicates when to transition between schedules.

Example
>>> linear = optim.linear_schedule(0, 1e-1, steps=10)
>>> cosine = optim.cosine_decay(1e-1, 200)
>>> lr_schedule = optim.join_schedules([linear, cosine], [10])
>>> optimizer = optim.Adam(learning_rate=lr_schedule)
>>> optimizer.learning_rate
array(0.0, dtype=float32)
>>> for _ in range(12): optimizer.update({}, {})
...
>>> optimizer.learning_rate
array(0.0999938, dtype=float32)

** Contents
