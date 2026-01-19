---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/features.html
---

# Feature extraction

**

- [.rst](../_sources/python/features.rst)
- **

.pdf

**

# Feature extraction

 Table of contents 

## Contents

# Feature extraction

This submodule provides some feature extraction utilities that can be used as
`key_transform` functions in MLX data pipelines. Even though a C++
implementation would allow for completely circumventing the GIL and better
utilization of multiple threads, we find that an efficient numpy implementation
can often be fast enough while providing signficiantly more flexibility.

## Audio Features

| WindowType(value) | Enum to choose the window function. |
| --- | --- |
| FrequencyScale(value) | Enum to choose the frequency scaling for the filter banks. |
| mfsc(n_filterbank, sampling_freq[, ...]) | Returns a function that computes spectrogram features from audio in particular mel-frequency spectral coefficients (MFSCs). |

** Contents
