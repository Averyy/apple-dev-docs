---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/transforms.html
---

# Transforms

**

- [.rst](../_sources/python/transforms.rst)
- **

.pdf

**

# Transforms

 Table of contents 

# Transforms

| eval(*args) | Evaluate anarrayor tree ofarray. |
| --- | --- |
| async_eval(*args) | Asynchronously evaluate anarrayor tree ofarray. |
| compile(fun[, inputs, outputs, shapeless]) | Returns a compiled function which produces the same output asfun. |
| checkpoint(fun) | Transform the passed callable to one that performs gradient checkpointing with respect to the inputs of the callable. |
| custom_function(*args, **kwargs) | Set up a function for custom gradient and vmap definitions. |
| disable_compile() | Globally disable compilation. |
| enable_compile() | Globally enable compilation. |
| grad(fun[, argnums, argnames]) | Returns a function which computes the gradient offun. |
| value_and_grad(fun[, argnums, argnames]) | Returns a function which computes the value and gradient offun. |
| jvp(fun, primals, tangents) | Compute the Jacobian-vector product. |
| vjp(fun, primals, cotangents) | Compute the vector-Jacobian product. |
| vmap(fun[, in_axes, out_axes]) | Returns a vectorized version offun. |
