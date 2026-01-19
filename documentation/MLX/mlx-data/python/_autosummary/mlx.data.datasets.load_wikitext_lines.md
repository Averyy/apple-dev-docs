---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.datasets.load_wikitext_lines.html
---

# mlx.data.datasets.load_wikitext_lines

**

- [.rst](../../_sources/python/_autosummary/mlx.data.datasets.load_wikitext_lines.rst)
- **

.pdf

**

# mlx.data.datasets.load_wikitext_lines

 Table of contents 

## Contents

# mlx.data.datasets.load_wikitext_lines

**mlx.data.datasets.load_wikitext_lines(*root=None*, *split='train'*, *subset='wikitext-103-raw'*, *quiet=False*, *validate_download=True*)**
: Fetch the WikiText dataset and load it as a stream of lines.

Parameters:

**root** (*Path** or *[str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The The directory to load/save the data. If
none is given the `~/.cache/mlx.data/wikitext` is used.
**split** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The split to use. It should be one of train, valid, test. (default: train)
**subset** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The subset to use. It should be one of wikitext-103,
wikitext-103-raw, wikitext-2, wikitext-2-raw . (default: wikitext-103-raw)
**quiet** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true do not show progress bars.

** Contents
