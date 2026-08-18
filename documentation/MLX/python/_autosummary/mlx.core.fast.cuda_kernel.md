---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.cuda_kernel.html
---

# mlx.core.fast.cuda_kernel

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.cuda_kernel.rst)
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

# mlx.core.fast.cuda_kernel

 Table of contents 

## Contents

# mlx.core.fast.cuda_kernel

**cuda_kernel(*name: str*, *input_names: Sequence[str]*, *output_names: Sequence[str]*, *source: str*, *header: str = ''*, *ensure_row_contiguous: bool = True*, *shared_memory: int = 0*) → [object](https://docs.python.org/3/library/functions.html#object)**
: A jit-compiled custom CUDA kernel defined from a source string.
This is the CUDA equivalent of [Custom Metal Kernels](../../dev/custom_metal_kernels.html#custom-metal-kernels).

Parameters:

**name** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Name for the kernel.
**input_names** (*List**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – The parameter names of the inputs in the
function signature.
**output_names** (*List**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – The parameter names of the outputs in the
function signature.
**source** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Source code. This is the body of a function in CUDA,
the function signature will be automatically generated.
**header** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Header source code to include before the main function.
Useful for helper functions or includes that should live outside of
the main function body.
**ensure_row_contiguous** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to ensure the inputs are row contiguous
before the kernel runs. Default: `True`.
**shared_memory** ([int](https://docs.python.org/3/library/functions.html#int)) – The dynamic shared memory to request for the
kernel. A value of 0 means no dynamic shared memory. Default: `0`.

Returns:
Callable `cuda_kernel`.

Example
def exp_elementwise(a: mx.array):
    source = '''
        auto elem = cooperative_groups::this_grid().thread_rank();
        T tmp = inp[elem];
        out[elem] = exp(tmp);
    '''

    kernel = mx.fast.cuda_kernel(
        name="myexp",
        input_names=["inp"],
        output_names=["out"],
        source=source
    )
    outputs = kernel(
        inputs=[a],
        template=[("T", mx.float32)],
        grid=(a.size, 1, 1),
        threadgroup=(256, 1, 1),
        output_shapes=[a.shape],
        output_dtypes=[a.dtype],
        verbose=True,
    )
    return outputs[0]

a = mx.random.normal(shape=(16, 16)).astype(mx.float16)
b = exp_elementwise(a)
assert mx.allclose(b, mx.exp(a))

** Contents
