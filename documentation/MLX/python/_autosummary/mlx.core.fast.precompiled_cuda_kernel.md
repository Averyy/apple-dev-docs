---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.precompiled_cuda_kernel.html
---

# mlx.core.fast.precompiled_cuda_kernel

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.precompiled_cuda_kernel.rst)
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

# mlx.core.fast.precompiled_cuda_kernel

 Table of contents 

## Contents

# mlx.core.fast.precompiled_cuda_kernel

**precompiled_cuda_kernel(**, name: str, compiled_source: bytes, inputs: collections.abc.Sequence[bool | int | float | mlx.core.array | ndarray[writable=False] | complex | mlx.core.ArrayLike], output_shapes: collections.abc.Sequence[tuple[int, ...]], output_dtypes: collections.abc.Sequence[mlx.core.Dtype], scalars: collections.abc.Sequence[object], grid: tuple[int, int, int], threadgroup: tuple[int, int, int], shared_memory: int = 0, init_value: float | None = None, ensure_row_contiguous: bool = False, stream: mlx.core.Stream | mlx.core.ThreadLocalStream | mlx.core.Device | mlx.core.DeviceType | None = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[array](mlx.core.array.html#mlx.core.array)]**
: Run a precompiled CUDA kernel defined from PTX or cubin.
This op is still experimental and various parts of the API may change.

Parameters:

**name** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Name for the kernel
**compiled_source** ([bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) – The precompiled kernel in raw bytes.
**inputs** (*List**[*[array](mlx.core.array.html#mlx.core.array)*]*) – The inputs passed to the CUDA kernel.
**output_shapes** (*List**[**Sequence**[*[int](https://docs.python.org/3/library/functions.html#int)*]**]*) – The list of shapes for each output.
**output_dtypes** (*List**[*[Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*]*) – The list of data types for each output.
**scalars** (*List**[**Union**[*[bool](https://docs.python.org/3/library/functions.html#bool)*, *[int](https://docs.python.org/3/library/functions.html#int)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**]*) – A list of scalar arguments to
pass to the kernel.
**grid** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*]*) – 3-tuple specifying the grid to launch the kernel with.
For compatibility with [metal_kernel()](mlx.core.fast.metal_kernel.html#mlx.core.fast.metal_kernel) the grid is in threads and not in threadblocks.
**threadgroup** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*]*) – 3-tuple specifying the threadgroup size to use.
**shared_memory** ([int](https://docs.python.org/3/library/functions.html#int)) – The dynamic shared memory to request for the
kernel. A value of 0 means no dynamic shared memory. Default: `0`.
**init_value** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Optional value to use to initialize all of the output arrays.
By default, output arrays are uninitialized. Default: `None`.
**ensure_row_contiguous** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to ensure the inputs are row contiguous
before the kernel runs. Default: `False`.
**stream** (*mx.stream**, **optional*) – Stream to run the kernel on. Default: `None`.

** Contents
