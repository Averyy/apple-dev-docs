---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.as_strided.html
---

# mlx.core.as_strided

```python
as_strided(a: array, /, shape: Sequence[int] | None = None, strides: Sequence[int] | None = None, offset: int = 0, *, stream: StreamOrDevice = None) → array
```

Create a view into the array with the given shape and strides.

The resulting array will always be as if the provided array was row
contiguous regardless of the provided arrays storage order and current
strides.

Note

Note that this function should be used with caution as it changes
the shape and strides of the array directly. This can lead to the
resulting array pointing to invalid memory locations which can
result into crashes.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array
- **shape** ([list](https://docs.python.org/3/builtins/stdtypes.html#list)([int](https://docs.python.org/3/builtins/functions.html#int)), *optional*) – The shape of the resulting array. If
None it defaults to `a.shape()`.
- **strides** ([list](https://docs.python.org/3/builtins/stdtypes.html#list)([int](https://docs.python.org/3/builtins/functions.html#int)), *optional*) – The strides of the resulting array. If
None it defaults to the reverse exclusive cumulative product of
`a.shape()`.
- **offset** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Skip that many elements from the beginning of the input
array.

**Returns:**
: The output array which is the strided view of the input.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
