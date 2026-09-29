---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.get_array_buffer_size.html
---

# mlx.core.get_array_buffer_size

**

- [.rst](../../_sources/python/_autosummary/mlx.core.get_array_buffer_size.rst)
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

# mlx.core.get_array_buffer_size

 Table of contents 

## Contents

# mlx.core.get_array_buffer_size

**get_array_buffer_size(**args*) → [int](https://docs.python.org/3/builtins/functions.html#int)**
: Get the size of the buffers backing arrays in bytes.
Each unique buffer is counted once. The full allocator size of each
buffer is used, which can exceed the logical size of its arrays. Arrays
must be evaluated before calling this function. The result does not
include graph objects, cached buffers, or other non-buffer memory.

Parameters:
***args** (*arrays** or **trees** of **arrays*) – Each argument can be a single array
or a tree of arrays. Leaves which are not arrays are ignored.

Returns:
The size of the unique buffers in bytes.

Return type:
[int](https://docs.python.org/3/builtins/functions.html#int)

** Contents
