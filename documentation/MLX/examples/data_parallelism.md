---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/examples/data_parallelism.html
---

# Data Parallelism

**

- [.rst](../_sources/examples/data_parallelism.rst)
- **

.pdf

**

**
**
**

**

# Data Parallelism

 Table of contents 

## Contents

# Data Parallelism

MLX enables efficient data parallel distributed training through its
distributed communication primitives.

## Training Example

In this section we will adapt an MLX training loop to support data parallel
distributed training. Namely, we will average the gradients across a set of
hosts before applying them to the model.

Our training loop looks like the following code snippet if we omit the model,
dataset, and optimizer initialization.

```
model = ...
optimizer = ...
dataset = ...

def step(model, x, y):
    loss, grads = loss_grad_fn(model, x, y)
    optimizer.update(model, grads)
    return loss

for x, y in dataset:
    loss = step(model, x, y)
    mx.eval(loss, model.parameters())
```

All we have to do to average the gradients across machines is perform an
`all_sum()` and divide by the size of the `Group`. Namely we
have to [mlx.utils.tree_map()](../python/_autosummary/mlx.utils.tree_map.html#mlx.utils.tree_map) the gradients with following function.

```
def all_avg(x):
    return mx.distributed.all_sum(x) / mx.distributed.init().size()
```

Putting everything together our training loop step looks as follows with
everything else remaining the same.

```
from mlx.utils import tree_map

def all_reduce_grads(grads):
    N = mx.distributed.init().size()
    if N == 1:
        return grads
    return tree_map(
        lambda x: mx.distributed.all_sum(x) / N,
        grads
    )

def step(model, x, y):
    loss, grads = loss_grad_fn(model, x, y)
    grads = all_reduce_grads(grads)  # <--- This line was added
    optimizer.update(model, grads)
    return loss
```

### Usingnn.average_gradients

Although the code example above works correctly; it performs one communication
per gradient. It is significantly more efficient to aggregate several gradients
together and perform fewer communication steps.

This is the purpose of [mlx.nn.average_gradients()](../python/_autosummary/mlx.nn.average_gradients.html#mlx.nn.average_gradients). The final code looks
almost identical to the example above:

```
model = ...
optimizer = ...
dataset = ...

def step(model, x, y):
    loss, grads = loss_grad_fn(model, x, y)
    grads = mx.nn.average_gradients(grads)  # <---- This line was added
    optimizer.update(model, grads)
    return loss

for x, y in dataset:
    loss = step(model, x, y)
    mx.eval(loss, model.parameters())
```

** Contents
