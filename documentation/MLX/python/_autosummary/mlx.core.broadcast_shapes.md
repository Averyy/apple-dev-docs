---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.broadcast_shapes.html
---

# mlx.core.broadcast_shapes

**

- [.rst](../../_sources/python/_autosummary/mlx.core.broadcast_shapes.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.broadcast_shapes

 Table of contents 

## Contents

# mlx.core.broadcast_shapes

**broadcast_shapes(**shapes: Sequence[int]*) → Tuple[[int](https://docs.python.org/3/library/functions.html#int)]**
: Broadcast shapes.
Returns the shape that results from broadcasting the supplied array shapes
against each other.

Parameters:
***shapes** (*Sequence**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The shapes to broadcast.

Returns:
The broadcasted shape.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)

Raises:
[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If the shapes cannot be broadcast.

Example
>>> mx.broadcast_shapes((1,), (3, 1))
(3, 1)
>>> mx.broadcast_shapes((6, 7), (5, 6, 1), (7,))
(5, 6, 7)
>>> mx.broadcast_shapes((5, 1, 4), (1, 3, 1))
(5, 3, 4)

** Contents
