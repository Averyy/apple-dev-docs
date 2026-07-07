---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_merge.html
---

# mlx.utils.tree_merge

**

- [.rst](../../_sources/python/_autosummary/mlx.utils.tree_merge.rst)
- **

.pdf

**

**
**
**

**

# mlx.utils.tree_merge

 Table of contents 

## Contents

# mlx.utils.tree_merge

**tree_merge(*tree_a*, *tree_b*, *merge_fn=None*)**
: Merge two Python trees in one containing the values of both. It can be
thought of as a deep dict.update method.

Parameters:

**tree_a** (*Any*) – The first Python tree.
**tree_b** (*Any*) – The second Python tree.
**merge_fn** (*callable**, **optional*) – A function to merge leaves.

Returns:
The Python tree containing the values of both `tree_a` and
`tree_b`.

** Contents
