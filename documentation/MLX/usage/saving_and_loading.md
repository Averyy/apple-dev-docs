---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/usage/saving_and_loading.html
---

# Saving and Loading Arrays

**

- [.rst](../_sources/usage/saving_and_loading.rst)
- **

.pdf

**

**
**
**

**

# Saving and Loading Arrays

 Table of contents 

# Saving and Loading Arrays

MLX supports multiple array serialization formats.

| Format | Extension | Function | Notes |
| --- | --- | --- | --- |
| NumPy | .npy | save() | Single arrays only |
| NumPy archive | .npz | savez()andsavez_compressed() | Multiple arrays |
| Safetensors | .safetensors | save_safetensors() | Multiple arrays |
| GGUF | .gguf | save_gguf() | Multiple arrays |

The [load()](../python/_autosummary/mlx.core.load.html#mlx.core.load) function will load any of the supported serialization
formats. It determines the format from the extensions. The output of
[load()](../python/_autosummary/mlx.core.load.html#mlx.core.load) depends on the format.

Here’s an example of saving a single array to a file:

```
>>> a = mx.array([1.0])
>>> mx.save("array", a)
```

The array `a` will be saved in the file `array.npy` (notice the extension
is automatically added). Including the extension is optional; if it is missing
it will be added. You can load the array with:

```
>>> mx.load("array.npy")
array([1], dtype=float32)
```

Here’s an example of saving several arrays to a single file:

```
>>> a = mx.array([1.0])
>>> b = mx.array([2.0])
>>> mx.savez("arrays", a, b=b)
```

For compatibility with [numpy.savez()](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez) the MLX [savez()](../python/_autosummary/mlx.core.savez.html#mlx.core.savez) takes arrays
as arguments. If the keywords are missing, then default names will be
provided. This can be loaded with:

```
>>> mx.load("arrays.npz")
{'b': array([2], dtype=float32), 'arr_0': array([1], dtype=float32)}
```

In this case [load()](../python/_autosummary/mlx.core.load.html#mlx.core.load) returns a dictionary of names to arrays.

The functions [save_safetensors()](../python/_autosummary/mlx.core.save_safetensors.html#mlx.core.save_safetensors) and [save_gguf()](../python/_autosummary/mlx.core.save_gguf.html#mlx.core.save_gguf) are similar to
[savez()](../python/_autosummary/mlx.core.savez.html#mlx.core.savez), but they take as input a [dict](https://docs.python.org/3/library/stdtypes.html#dict) of string names to arrays:

```
>>> a = mx.array([1.0])
>>> b = mx.array([2.0])
>>> mx.save_safetensors("arrays", {"a": a, "b": b})
```
