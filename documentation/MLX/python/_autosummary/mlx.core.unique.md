---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.unique.html
---

# mlx.core.unique

```python
unique(a: array, /, size: int, return_index: bool = False, return_inverse: bool = False, return_counts: bool = False, fill_value: scalar | array | None = None, *, stream: StreamOrDevice = None) → array | tuple[array, ...]
```

Returns the sorted unique elements of the flattened array.

The shape of the output does not depend on the values in `a`, so
`a` is not evaluated. Unlike NumPy, the size is never inferred from
the values and must be provided.

Entries past the last unique element hold `fill_value` and their
count is `0`, so `mx.sum(counts > 0)` gives the number of unique
elements as long as the output is not truncated.

A truncated output keeps the smallest `size` unique elements, and
`index`, `inverse` and `counts` then stop describing all of `a`,
and `inverse` and `counts` stop agreeing with each other: the counts
of the dropped elements are gone, while their indices in `inverse` are
clamped to the last entry.
`inverse` is meaningless for a `size` of `0`, since there is no
element left for it to point at.

This op builds on `mx.sort`, so a `bool` input needs the CPU
stream, which is where `mx.sort` supports it.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **size** ([int](https://docs.python.org/3/builtins/functions.html#int)) – The size of the output. If the size is smaller than
the number of unique elements of `a`, the output is truncated.
If it is larger, the output is padded with `fill_value`.
- **return_index** ([bool](https://docs.python.org/3/builtins/functions.html#bool), *optional*) – If `True`, also return the index
in the flattened `a` of the first occurrence of each unique
element. Default: `False`.
- **return_inverse** ([bool](https://docs.python.org/3/builtins/functions.html#bool), *optional*) – If `True`, also return the
indices of the unique array that rebuild `a`. The indices have
the same shape as `a`. Default: `False`.
- **return_counts** ([bool](https://docs.python.org/3/builtins/functions.html#bool), *optional*) – If `True`, also return the number
of times each unique element occurs in `a`. Default: `False`.
- **fill_value** (*scalar* *or* [array](mlx.core.array.md#mlx.core.array), *optional*) – The value of the entries
past the last unique element. If `None`, this defaults to the
first of the sorted unique elements. Default: `None`.

**Returns:**
: The sorted unique elements. If any of
`return_index`, `return_inverse` or `return_counts` is
`True`, a tuple with the requested arrays in the order values,
index, inverse, counts.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array) or [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([array](mlx.core.array.md#mlx.core.array), …)

Example

```
>>> a = mx.array([2, 1, 2, 3, 1])
>>> mx.unique(a, 3)
array([1, 2, 3], dtype=int32)
>>> mx.unique(a, 5)
array([1, 2, 3, 1, 1], dtype=int32)
>>> values, index, inverse, counts = mx.unique(
...     a, 4, True, True, True, fill_value=0)
>>> values
array([1, 2, 3, 0], dtype=int32)
>>> index
array([1, 0, 3, 1], dtype=uint32)
>>> inverse
array([1, 0, 1, 2, 0], dtype=uint32)
>>> counts
array([2, 2, 1, 0], dtype=int32)
```
