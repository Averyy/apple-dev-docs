---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adafactor.html
---

# mlx.optimizers.Adafactor

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adafactor.rst)
- **

.pdf

**

# mlx.optimizers.Adafactor

 Table of contents 

## Contents

# mlx.optimizers.Adafactor

**class Adafactor(*learning_rate: float | Callable[[array], array] | None = None*, *eps: Tuple[float, float] = (1e-30, 0.001)*, *clip_threshold: float = 1.0*, *decay_rate: float = -0.8*, *beta_1: float | None = None*, *weight_decay: float = 0.0*, *scale_parameter: bool = True*, *relative_step: bool = True*, *warmup_init: bool = False*)**
: The Adafactor optimizer.
Our Adafactor implementation follows the original paper: [Adafactor:
Adaptive Learning Rates with Sublinear Memory Cost](https://arxiv.org/abs/1804.04235)

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable**, **optional*) – The learning rate.
Default: `None`.
**eps** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[float](https://docs.python.org/3/library/functions.html#float)*, *[float](https://docs.python.org/3/library/functions.html#float)*)**, **optional*) – The first term \(\epsilon_1\)
added to the square of the gradients to improve numerical
stability and the second term \(\epsilon_2\) is used for
parameter scaling if `parameter_scale` is set to `True`.
Default: `(1e-30, 1e-3)`.
**clip_threshold** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Clips the unscaled update at
`clip_threshold`. Default: `1.0`.
**decay_rate** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Coefficient for the running average
of the squared gradient. Default: `-0.8`.
**beta_1** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – If set to a value bigger than zero
then first moment will be used. Default: `None`.
**weight_decay** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The weight decay \(\lambda\).
Default: `0.0`.
**scale_parameter** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True` the learning rate
will be scaled by \(\max(\epsilon_1, \text{RMS}(w_{t-1}))\).
Default: `True`.
**relative_step** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True` the `learning_rate`
will be ignored and relative step size will be computed.
Default: `True`.
**warmup_init** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True` then the relative
step size will be calculated by the current step. Default:
`False`.

Methods

`__init__`([learning_rate, eps, ...])

`apply_single`(gradient, parameter, state)
Performs the Adafactor parameter and state update.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
