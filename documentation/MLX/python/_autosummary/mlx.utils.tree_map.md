---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_map.html
---

# mlx.utils.tree_map

**

- [.rst](../../_sources/python/_autosummary/mlx.utils.tree_map.rst)
- **

.pdf

**

**
**
**

**

# mlx.utils.tree_map

 Table of contents 

## Contents

# mlx.utils.tree_map

**tree_map(*fn: Callable*, *tree: Any*, **rest: Any*, *is_leaf: Callable | None = None*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)**
: Applies `fn` to the leaves of the Python tree `tree` and
returns a new collection with the results.
If `rest` is provided, every item is assumed to be a superset of `tree`
and the corresponding leaves are provided as extra positional arguments to
`fn`. In that respect, [tree_map()](#mlx.utils.tree_map) is closer to [itertools.starmap()](https://docs.python.org/3/library/itertools.html#itertools.starmap)
than to [map()](https://docs.python.org/3/library/functions.html#map).
The keyword argument `is_leaf` decides what constitutes a leaf from
`tree` similar to [tree_flatten()](mlx.utils.tree_flatten.html#mlx.utils.tree_flatten).
import mlx.nn as nn
from mlx.utils import tree_map

model = nn.Linear(10, 10)
print(model.parameters().keys())
# dict_keys(['weight', 'bias'])

# square the parameters
model.update(tree_map(lambda x: x*x, model.parameters()))

Parameters:

**fn** (*callable*) – The function that processes the leaves of the tree.
**tree** (*Any*) – The main Python tree that will be iterated upon.
**rest** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Any**]*) – Extra trees to be iterated together with `tree`.
**is_leaf** (*callable**, **optional*) – An optional callable that returns `True`
if the passed object is considered a leaf or `False` otherwise.

Returns:
A Python tree with the new values returned by `fn`.

** Contents
