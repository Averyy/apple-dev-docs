---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.save_weights.html
---

# mlx.nn.Module.save_weights

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.save_weights.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.Module.save_weights

 Table of contents 

## Contents

# mlx.nn.Module.save_weights

**Module.save_weights(*file: str*)**
: Save the model’s weights to a file. The saving method is determined by the file extension:
- `.npz` will use `mx.savez()`
- `.safetensors` will use `mx.save_safetensors()`

** Contents
