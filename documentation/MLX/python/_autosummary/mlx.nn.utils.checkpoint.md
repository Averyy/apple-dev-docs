---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.utils.checkpoint.html
---

# mlx.nn.utils.checkpoint

```python
checkpoint(module: Module, fn: Callable | None = None)
```

Transform the passed callable to one that performs gradient
checkpointing with respect to the trainable parameters of the module (and
the callable’s inputs).

**Parameters:**

- **module** ([Module](../nn/module.md#mlx.nn.Module)) – The module for whose parameters we will be
performing gradient checkpointing.
- **fn** (*Callable*, *optional*) – The function to checkpoint. If not provided it
defaults to the provided module.

**Returns:**
: A callable that saves the inputs and outputs during the forward pass
and recomputes all intermediate states during the backward pass.
