---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/transforms.html
---

# Transforms

| [eval](_autosummary/mlx.core.eval.md#mlx.core.eval)(*args) | Evaluate an [array](_autosummary/mlx.core.array.md#mlx.core.array) or tree of [array](_autosummary/mlx.core.array.md#mlx.core.array). |
| --- | --- |
| [async_eval](_autosummary/mlx.core.async_eval.md#mlx.core.async_eval)(*args) | Asynchronously evaluate an [array](_autosummary/mlx.core.array.md#mlx.core.array) or tree of [array](_autosummary/mlx.core.array.md#mlx.core.array). |
| [compile](_autosummary/mlx.core.compile.md#mlx.core.compile)(fun[, inputs, outputs, shapeless]) | Returns a compiled function which produces the same output as `fun`. |
| [checkpoint](_autosummary/mlx.core.checkpoint.md#mlx.core.checkpoint)(fun) | Transform the passed callable to one that performs gradient checkpointing with respect to the inputs of the callable. |
| [custom_function](_autosummary/mlx.core.custom_function.md#mlx.core.custom_function)(*args, **kwargs) | Set up a function for custom gradient and vmap definitions. |
| [disable_compile](_autosummary/mlx.core.disable_compile.md#mlx.core.disable_compile)() | Globally disable compilation. |
| [enable_compile](_autosummary/mlx.core.enable_compile.md#mlx.core.enable_compile)() | Globally enable compilation. |
| [grad](_autosummary/mlx.core.grad.md#mlx.core.grad)(fun[, argnums, argnames]) | Returns a function which computes the gradient of `fun`. |
| [value_and_grad](_autosummary/mlx.core.value_and_grad.md#mlx.core.value_and_grad)(fun[, argnums, argnames]) | Returns a function which computes the value and gradient of `fun`. |
| [jvp](_autosummary/mlx.core.jvp.md#mlx.core.jvp)(fun, primals, tangents) | Compute the Jacobian-vector product. |
| [vjp](_autosummary/mlx.core.vjp.md#mlx.core.vjp)(fun, primals, cotangents) | Compute the vector-Jacobian product. |
| [vmap](_autosummary/mlx.core.vmap.md#mlx.core.vmap)(fun[, in_axes, out_axes]) | Returns a vectorized version of `fun`. |
