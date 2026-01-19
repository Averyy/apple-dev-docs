---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/module.html
---

# Module

**

- [.rst](../../_sources/python/nn/module.rst)
- **

.pdf

**

# Module

 Table of contents 

## Contents

# Module

**class Module**
: Base class for building neural networks with MLX.
All the layers provided in `mlx.nn.layers` subclass this class and
your models should do the same.
A `Module` can contain other `Module` instances or [mlx.core.array](../_autosummary/mlx.core.array.html#mlx.core.array)
instances in arbitrary nesting of python lists or dicts. The `Module`
then allows recursively extracting all the [mlx.core.array](../_autosummary/mlx.core.array.html#mlx.core.array) instances
using [mlx.nn.Module.parameters()](_autosummary/mlx.nn.Module.parameters.html#mlx.nn.Module.parameters).
In addition, the `Module` has the concept of trainable and non trainable
parameters (called “frozen”). When using [mlx.nn.value_and_grad()](../_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad)
the gradients are returned only with respect to the trainable parameters.
All arrays in a module are trainable unless they are added in the “frozen”
set by calling [freeze()](_autosummary/mlx.nn.Module.freeze.html#mlx.nn.Module.freeze).
import mlx.core as mx
import mlx.nn as nn

class MyMLP(nn.Module):
    def __init__(self, in_dims: int, out_dims: int, hidden_dims: int = 16):
        super().__init__()

        self.in_proj = nn.Linear(in_dims, hidden_dims)
        self.out_proj = nn.Linear(hidden_dims, out_dims)

    def __call__(self, x):
        x = self.in_proj(x)
        x = mx.maximum(x, 0)
        return self.out_proj(x)

model = MyMLP(2, 1)

# All the model parameters are created but since MLX is lazy by
# default, they are not evaluated yet. Calling `mx.eval` actually
# allocates memory and initializes the parameters.
mx.eval(model.parameters())

# Setting a parameter to a new value is as simply as accessing that
# parameter and assigning a new array to it.
model.in_proj.weight = model.in_proj.weight * 2
mx.eval(model.parameters())

Attributes

[Module.training](_autosummary/mlx.nn.Module.training.html#mlx.nn.Module.training)
Boolean indicating if the model is in training mode.

[Module.state](_autosummary/mlx.nn.Module.state.html#mlx.nn.Module.state)
The module's state dictionary

Methods

[Module.apply](_autosummary/mlx.nn.Module.apply.html#mlx.nn.Module.apply)(map_fn[, filter_fn])
Map all the parameters using the provided `map_fn` and immediately update the module with the mapped parameters.

[Module.apply_to_modules](_autosummary/mlx.nn.Module.apply_to_modules.html#mlx.nn.Module.apply_to_modules)(apply_fn)
Apply a function to all the modules in this instance (including this instance).

[Module.children](_autosummary/mlx.nn.Module.children.html#mlx.nn.Module.children)()
Return the direct descendants of this Module instance.

[Module.eval](_autosummary/mlx.nn.Module.eval.html#mlx.nn.Module.eval)()
Set the model to evaluation mode.

[Module.filter_and_map](_autosummary/mlx.nn.Module.filter_and_map.html#mlx.nn.Module.filter_and_map)(filter_fn[, map_fn, ...])
Recursively filter the contents of the module using `filter_fn`, namely only select keys and values where `filter_fn` returns true.

[Module.freeze](_autosummary/mlx.nn.Module.freeze.html#mlx.nn.Module.freeze)(*[, recurse, keys, strict])
Freeze the Module's parameters or some of them.

[Module.leaf_modules](_autosummary/mlx.nn.Module.leaf_modules.html#mlx.nn.Module.leaf_modules)()
Return the submodules that do not contain other modules.

[Module.load_weights](_autosummary/mlx.nn.Module.load_weights.html#mlx.nn.Module.load_weights)(file_or_weights[, strict])
Update the model's weights from a `.npz`, a `.safetensors` file, or a list.

[Module.modules](_autosummary/mlx.nn.Module.modules.html#mlx.nn.Module.modules)()
Return a list with all the modules in this instance.

[Module.named_modules](_autosummary/mlx.nn.Module.named_modules.html#mlx.nn.Module.named_modules)()
Return a list with all the modules in this instance and their name with dot notation.

[Module.parameters](_autosummary/mlx.nn.Module.parameters.html#mlx.nn.Module.parameters)()
Recursively return all the [mlx.core.array](../_autosummary/mlx.core.array.html#mlx.core.array) members of this Module as a dict of dicts and lists.

[Module.save_weights](_autosummary/mlx.nn.Module.save_weights.html#mlx.nn.Module.save_weights)(file)
Save the model's weights to a file.

[Module.set_dtype](_autosummary/mlx.nn.Module.set_dtype.html#mlx.nn.Module.set_dtype)(dtype, predicate, ...)
Set the dtype of the module's parameters.

[Module.train](_autosummary/mlx.nn.Module.train.html#mlx.nn.Module.train)([mode])
Set the model in or out of training mode.

[Module.trainable_parameters](_autosummary/mlx.nn.Module.trainable_parameters.html#mlx.nn.Module.trainable_parameters)()
Recursively return all the non frozen [mlx.core.array](../_autosummary/mlx.core.array.html#mlx.core.array) members of this Module as a dict of dicts and lists.

[Module.unfreeze](_autosummary/mlx.nn.Module.unfreeze.html#mlx.nn.Module.unfreeze)(*[, recurse, keys, strict])
Unfreeze the Module's parameters or some of them.

[Module.update](_autosummary/mlx.nn.Module.update.html#mlx.nn.Module.update)(parameters[, strict])
Replace the parameters of this Module with the provided ones in the dict of dicts and lists.

[Module.update_modules](_autosummary/mlx.nn.Module.update_modules.html#mlx.nn.Module.update_modules)(modules[, strict])
Replace the child modules of this [Module](#mlx.nn.Module) instance with the provided ones in the dict of dicts and lists.

** Contents
