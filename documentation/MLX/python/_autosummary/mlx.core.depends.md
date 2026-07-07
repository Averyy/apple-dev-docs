---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.depends.html
---

# mlx.core.depends

**

- [.rst](../../_sources/python/_autosummary/mlx.core.depends.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.depends

 Table of contents 

## Contents

# mlx.core.depends

**depends(*inputs: array | Sequence[array]*, *dependencies: array | Sequence[array]*)**
: Insert dependencies between arrays in the graph. The outputs are
identical to `inputs` but with dependencies on `dependencies`.

Parameters:

**inputs** ([array](mlx.core.array.html#mlx.core.array)* or **Sequence**[*[array](mlx.core.array.html#mlx.core.array)*]*) – The input array or arrays.
**dependencies** ([array](mlx.core.array.html#mlx.core.array)* or **Sequence**[*[array](mlx.core.array.html#mlx.core.array)*]*) – The array or arrays
to insert dependencies on.

Returns:
The outputs which depend on dependencies.

Return type:
[array](mlx.core.array.html#mlx.core.array) or *Sequence*[[array](mlx.core.array.html#mlx.core.array)]

** Contents
