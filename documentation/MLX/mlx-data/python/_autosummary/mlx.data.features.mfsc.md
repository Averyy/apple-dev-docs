---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.features.mfsc.html
---

# mlx.data.features.mfsc

**

- [.rst](../../_sources/python/_autosummary/mlx.data.features.mfsc.rst)
- **

.pdf

**

# mlx.data.features.mfsc

 Table of contents 

## Contents

# mlx.data.features.mfsc

**mlx.data.features.mfsc(*n_filterbank*, *sampling_freq*, *frame_size_ms=25*, *frame_stride_ms=10*, *pre_emphasis_coeff=0.97*, *window_type=WindowType.Hamming*, *low_freq=0*, *high_freq=-1*, *mel_floor=1.0*, *freq_scale=FrequencyScale.MEL*, *post_process=None*)**
: Returns a function that computes spectrogram features from audio in
particular mel-frequency spectral coefficients (MFSCs).

Note
This feature extractor operates on mono audio provided as a 1D array.
Meaning the input should have shape `(N,)` and not `(N, 1)`. You may
want to look into [squeeze()](mlx.data.Buffer.squeeze.html#mlx.data.Buffer.squeeze) to transform arrays of shape
`(N, 1)` to `(N,)`.

The featurization function

computes a sliding window of the input audio
applies a pre-emphasis filter
applies a windowing function
computes the power spectrum
computes triangular filterbank features
compute the log of the features
apply any post processing function that may be provided

The following example loads the librispeech dataset and computes MFSC
features:
from mlx.data.datasets import load_librispeech
from mlx.data.features import mfsc

dset = (
    load_librispeech()
    .squeeze("audio")
    .key_transform("audio", mfsc(80, 16000))
    .to_stream()
    .prefetch(16, 8)
    .batch(16)
    .prefetch(2, 1)
)

Parameters:

**n_filterbank** ([int](https://docs.python.org/3/library/functions.html#int)) – How many frequency bands to use. This number will
be the dimensionality of the resulting features.
**sampling_freq** ([int](https://docs.python.org/3/library/functions.html#int)) – The sampling frequency of the input audio in Hz.
**frame_size_ms** ([int](https://docs.python.org/3/library/functions.html#int)) – Each output feature will correspond to that many
milliseconds of input audio. (default: 25)
**frame_stride_ms** ([int](https://docs.python.org/3/library/functions.html#int)) – Two consecutive features will correspond to
audio windows that are that many milliseconds apart. (default: 10)
**pre_emphasis_coeff** ([float](https://docs.python.org/3/library/functions.html#float)) – Defines the free parameter of the FIR
filter that does the pre-emphasis. (default: 0.97)
**window_type** ([WindowType](mlx.data.features.WindowType.html#mlx.data.features.WindowType)) – Defines the windowing function to use before
computing the power spectrum. (default: WindowType.Hamming)
**low_freq** ([int](https://docs.python.org/3/library/functions.html#int)) – The lowest frequency to use when creating the frequency
bands. Simply put, signal power in lower frequencies is ignored.
(default: 0)
**high_freq** ([int](https://docs.python.org/3/library/functions.html#int)) – The highest frequency to use when creating the frequency
bands. Simply put, signal power in higher frequencies is ignored.
If set to -1 then `sampling_freq // 2` is used.  (default: -1)
**mel_floor** ([float](https://docs.python.org/3/library/functions.html#float)) – The minimum power collected in the filterbanks. Even
though the name is `mel_floor` this applies even when using different
frequency scales. (default: 1.0)
**freq_scale** ([FrequencyScale](mlx.data.features.FrequencyScale.html#mlx.data.features.FrequencyScale)) – The frequency scale to use when computing
the frequency bands for the filterbanks. (default: FrequencyScale.MEL)
**post_process** (*callable**, **optional*) – An optional callable to post process
the MFSC features. (default: None)

** Contents
