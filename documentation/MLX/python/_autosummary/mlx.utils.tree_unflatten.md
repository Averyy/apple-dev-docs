---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_unflatten.html
---

# mlx.utils.tree_unflatten

**

- [.rst](../../_sources/python/_autosummary/mlx.utils.tree_unflatten.rst)
- **

.pdf

**

# mlx.utils.tree_unflatten

 Table of contents 

## Contents

# mlx.utils.tree_unflatten

**tree_unflatten(*tree: List[Tuple[str, Any]] | Dict[str, Any]*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)**
: Recreate a Python tree from its flat representation.
from mlx.utils import tree_unflatten

d = tree_unflatten([("hello.world", 42)])
print(d)
# {"hello": {"world": 42}}

d = tree_unflatten({"hello.world": 42})
print(d)
# {"hello": {"world": 42}}

Parameters:
**tree** ([list](https://docs.python.org/3/library/stdtypes.html#list)*[*[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*, **Any**]**] or *[dict](https://docs.python.org/3/library/stdtypes.html#dict)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*, **Any**]*) – The flat representation of a Python tree.
For instance as returned by [tree_flatten()](mlx.utils.tree_flatten.html#mlx.utils.tree_flatten).

Returns:
A Python tree.

** Contents
