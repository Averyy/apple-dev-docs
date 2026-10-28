---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_unflatten.html
---

# mlx.utils.tree_unflatten

```python
tree_unflatten(tree: List[Tuple[str, Any]] | Dict[str, Any]) → Any
```

Recreate a Python tree from its flat representation.

```
from mlx.utils import tree_unflatten

d = tree_unflatten([("hello.world", 42)])
print(d)
# {"hello": {"world": 42}}

d = tree_unflatten({"hello.world": 42})
print(d)
# {"hello": {"world": 42}}
```

**Parameters:**
: **tree** ([list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), *Any*]*] or* [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), *Any*]) – The flat representation of a
Python tree. For instance as returned by [tree_flatten()](mlx.utils.tree_flatten.md#mlx.utils.tree_flatten).

**Returns:**
: A Python tree.
