---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.asarray.html
---

# mlx.core.asarray

```python
asarray(a: scalar | array | Sequence | DLPackCompatible, dtype: Dtype | None = None, *, copy: bool | None = None) → array
```

Convert the input to an array.

**Parameters:**

- **a** – Input data.
- **dtype** ([Dtype](mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – The desired data-type for the array.
- **copy** ([bool](https://docs.python.org/3/builtins/functions.html#bool), *optional*) – Whether to copy the input. If `True`,
always copy. If `False`, never copy. If `None`, share memory
when possible and copy otherwise. Zero-copy DLPack imports
preserve the DLPack strides.

**Returns:**
: An array interpretation of the input.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)

**Raises:**
: [ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError) – If `copy` is `False` and a copy is required.
