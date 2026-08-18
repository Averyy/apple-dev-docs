---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_flatten.html
---

# mlx.utils.tree_flatten

**

- [.rst](../../_sources/python/_autosummary/mlx.utils.tree_flatten.rst)
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

# mlx.utils.tree_flatten

 Table of contents 

## Contents

# mlx.utils.tree_flatten

**tree_flatten(*tree: Any*, *prefix: str = ''*, *is_leaf: Callable | None = None*, *destination: List[Tuple[str, Any]] | Dict[str, Any] | None = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List)[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]**
: Flattens a Python tree to a list of key, value tuples.
The keys are using the dot notation to define trees of arbitrary depth and
complexity.
from mlx.utils import tree_flatten

print(tree_flatten([[[0]]]))
# [("0.0.0", 0)]

print(tree_flatten([[[0]]], prefix=".hello"))
# [("hello.0.0.0", 0)]

tree_flatten({"a": {"b": 1}}, destination={})
{"a.b": 1}

Note
Dictionaries should have keys that are valid Python identifiers.

Parameters:

**tree** (*Any*) – The Python tree to be flattened.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – A prefix to use for the keys. The first character is
always discarded.
**is_leaf** (*callable*) – An optional callable that returns True if the
passed object is considered a leaf or False otherwise.
**destination** ([list](https://docs.python.org/3/library/stdtypes.html#list)* or *[dict](https://docs.python.org/3/library/stdtypes.html#dict)*, **optional*) – A list or dictionary to store the
flattened tree. If None an empty list will be used. Default: `None`.

Returns:

The flat representation ofthe Python tree.

Return type:
*Union*[*List*[*Tuple*[[str](https://docs.python.org/3/library/stdtypes.html#str), *Any*]], *Dict*[[str](https://docs.python.org/3/library/stdtypes.html#str), *Any*]]

** Contents
