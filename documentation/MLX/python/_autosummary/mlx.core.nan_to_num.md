---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.nan_to_num.html
---

# mlx.core.nan_to_num

**

- [.rst](../../_sources/python/_autosummary/mlx.core.nan_to_num.rst)
- **

.pdf

**

# mlx.core.nan_to_num

 Table of contents 

## Contents

# mlx.core.nan_to_num

**nan_to_num(*a: scalar | array*, *nan: float = 0*, *posinf: float | None = None*, *neginf: float | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Replace NaN and Inf values with finite numbers.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**nan** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Value to replace NaN with. Default: `0`.
**posinf** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Value to replace positive infinities
with. If `None`, defaults to largest finite value for the
given data type. Default: `None`.
**neginf** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Value to replace negative infinities
with. If `None`, defaults to the negative of the largest
finite value for the given data type. Default: `None`.

Returns:
Output array with NaN and Inf replaced.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
