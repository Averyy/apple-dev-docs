---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.Group.html
---

# mlx.core.distributed.Group

```python
class Group
```

An [mlx.core.distributed.Group](#mlx.core.distributed.Group) represents a group of independent mlx
processes that can communicate.

```python
__init__(*args, **kwargs)
```

Methods

| [__init__](#mlx.core.distributed.Group.__init__)(*args, **kwargs) |  |
| --- | --- |
| `rank`(self) | Get the rank of this process |
| `size`(self) | Get the size of the group |
| `split`(self, color[, key]) | Split the group to subgroups based on the provided color. |
