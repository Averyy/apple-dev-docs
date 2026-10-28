---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.softmax.html
---

# mlx.core.softmax

```python
softmax(a: array, /, axis: None | int | Sequence[int] = None, *, precise: bool = False, stream: StreamOrDevice = None) → array
```

Perform the softmax along the given axis.

This operation is a numerically stable version of:

```
exp(a) / sum(exp(a), axis, keepdims=True)
```

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **axis** ([int](https://docs.python.org/3/builtins/functions.html#int) *or* [list](https://docs.python.org/3/builtins/stdtypes.html#list)([int](https://docs.python.org/3/builtins/functions.html#int)), *optional*) – Optional axis or axes to compute
the softmax over. If unspecified this performs the softmax over
the full array.
- **precise** ([bool](https://docs.python.org/3/builtins/functions.html#bool), *optional*) – Accumulate in `float32` for inputs of
lower precision. Otherwise the accumulation type matches the
input, which can lose precision over long reduction axes.
Default: `False`.

**Returns:**
: The output of the softmax.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
