---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_map_with_path.html
---

# mlx.utils.tree_map_with_path

**

- [.rst](../../_sources/python/_autosummary/mlx.utils.tree_map_with_path.rst)
- **

.pdf

**

# mlx.utils.tree_map_with_path

 Table of contents 

## Contents

# mlx.utils.tree_map_with_path

**tree_map_with_path(*fn: Callable*, *tree: Any*, **rest: Any*, *is_leaf: Callable | None = None*, *path: Any | None = None*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)**
: Applies `fn` to the path and leaves of the Python tree `tree` and
returns a new collection with the results.
This function is the same [tree_map()](mlx.utils.tree_map.html#mlx.utils.tree_map) but the `fn` takes the path as
the first argument followed by the remaining tree nodes.

Parameters:

**fn** (*callable*) – The function that processes the leaves of the tree.
**tree** (*Any*) – The main Python tree that will be iterated upon.
**rest** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Any**]*) – Extra trees to be iterated together with `tree`.
**is_leaf** (*Optional**[**Callable**]*) – An optional callable that returns `True`
if the passed object is considered a leaf or `False` otherwise.
**path** (*Optional**[**Any**]*) – Prefix will be added to the result.

Returns:
A Python tree with the new values returned by `fn`.

Example
>>> from mlx.utils import tree_map_with_path
>>> tree = {"model": [{"w": 0, "b": 1}, {"w": 0, "b": 1}]}
>>> new_tree = tree_map_with_path(lambda path, _: print(path), tree)
model.0.w
model.0.b
model.1.w
model.1.b

** Contents
