---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/tree_utils.html
---

# Tree Utils

In MLX we consider a python tree to be an arbitrarily nested collection of
dictionaries, lists and tuples without cycles. Functions in this module that
return python trees will be using the default python `dict`, `list` and
`tuple` but they can usually process objects that inherit from any of these.

Note

Dictionaries should have keys that are valid python identifiers.

| [tree_flatten](_autosummary/mlx.utils.tree_flatten.md#mlx.utils.tree_flatten)(tree[, prefix, is_leaf, ...]) | Flattens a Python tree to a list of key, value tuples. |
| --- | --- |
| [tree_unflatten](_autosummary/mlx.utils.tree_unflatten.md#mlx.utils.tree_unflatten)(tree) | Recreate a Python tree from its flat representation. |
| [tree_map](_autosummary/mlx.utils.tree_map.md#mlx.utils.tree_map)(fn, tree, *rest[, is_leaf]) | Applies `fn` to the leaves of the Python tree `tree` and returns a new collection with the results. |
| [tree_map_with_path](_autosummary/mlx.utils.tree_map_with_path.md#mlx.utils.tree_map_with_path)(fn, tree, *rest[, ...]) | Applies `fn` to the path and leaves of the Python tree `tree` and returns a new collection with the results. |
| [tree_reduce](_autosummary/mlx.utils.tree_reduce.md#mlx.utils.tree_reduce)(fn, tree[, initializer, is_leaf]) | Applies a reduction to the leaves of a Python tree. |
| [tree_merge](_autosummary/mlx.utils.tree_merge.md#mlx.utils.tree_merge)(tree_a, tree_b[, merge_fn]) | Merge two Python trees in one containing the values of both. |
