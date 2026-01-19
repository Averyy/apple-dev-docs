---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/tree_utils.html
---

# Tree Utils

**

- [.rst](../_sources/python/tree_utils.rst)
- **

.pdf

**

# Tree Utils

 Table of contents 

# Tree Utils

In MLX we consider a python tree to be an arbitrarily nested collection of
dictionaries, lists and tuples without cycles. Functions in this module that
return python trees will be using the default python `dict`, `list` and
`tuple` but they can usually process objects that inherit from any of these.

Note

Dictionaries should have keys that are valid python identifiers.

| tree_flatten(tree[, prefix, is_leaf, ...]) | Flattens a Python tree to a list of key, value tuples. |
| --- | --- |
| tree_unflatten(tree) | Recreate a Python tree from its flat representation. |
| tree_map(fn, tree, *rest[, is_leaf]) | Appliesfnto the leaves of the Python treetreeand returns a new collection with the results. |
| tree_map_with_path(fn, tree, *rest[, ...]) | Appliesfnto the path and leaves of the Python treetreeand returns a new collection with the results. |
| tree_reduce(fn, tree[, initializer, is_leaf]) | Applies a reduction to the leaves of a Python tree. |
