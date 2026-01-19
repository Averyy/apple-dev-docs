---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.datasets.load_speechcommands.html
---

# mlx.data.datasets.load_speechcommands

**

- [.rst](../../_sources/python/_autosummary/mlx.data.datasets.load_speechcommands.rst)
- **

.pdf

**

# mlx.data.datasets.load_speechcommands

 Table of contents 

## Contents

# mlx.data.datasets.load_speechcommands

**mlx.data.datasets.load_speechcommands(*root=None*, *split='train'*, *quiet=False*, *validate_download=True*)**
: Load the Speech Commands (v0.0.2) [1] dataset directly from the TAR archive.

Parameters:

**root** (*Path** or *[str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The The directory to load/save the data. If
none is given the `~/.cache/mlx.data/speechcommands` is used.
**split** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The split to use. It should be one of train,
validation or test
**quiet** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true do not show download (and possibly decompression)
progress.

References
[1] Warden, Pete. “Speech commands: A dataset for limited-vocabulary speech recognition.” arXiv preprint arXiv:1804.03209 (2018).

** Contents
