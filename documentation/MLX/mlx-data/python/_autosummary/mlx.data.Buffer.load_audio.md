---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.load_audio.html
---

# mlx.data.Buffer.load_audio

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.load_audio.rst)
- **

.pdf

**

# mlx.data.Buffer.load_audio

 Table of contents 

## Contents

# mlx.data.Buffer.load_audio

**Buffer.load_audio(*self: mlx.data._c.Buffer*, *key: str*, *prefix: str = ''*, *info: bool = False*, *from_memory: bool = False*, *info_type: mlx.data._c.LoadAudioInfo = <LoadAudioInfo.All: 0>*, *sample_rate: int = 0*, *resampling_quality: str = 'sinc-fastest'*, *info_key: str = ''*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Load an audio file.
Decodes audio from an audio file on disk or in memory. It can also load
the audio info instead. If a sample rate is provided it resamples the
audio to the requested rate.
If `info_type` is set to `LoadAudioInfo.All` then the result will
contain the number of frames, the number of channels and the sampling
rate of the audio file.
It can also be set to `LoadAudioInfo.NumFrames`,
`LoadAudioInfo.NumChannels`, `LoadAudioInfo.SampleRate` and
`LoadAudioInfo.NumSeconds` to load the corresponding information.
The following example filters from the `Stream` all audio files that
are less than 10 seconds long.
dset = (
  dset
  .load_audio("audio_file", info=True, info_type=LoadAudioInfo.NumSeconds, output_key="audio_info")
  .sample_transform(lambda s: s if s["audio_info"] >= 10 else dict())
)

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use when loading the audio files.
**info** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If set to True load the audio file information instead
of the data in `output_key`, when `info_key` is not provided. (default: False)
**from_memory** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true assume the file contents are in the array
instead of the file name. (default: False)
**info_type** (*LoadAudioInfo*) – If `info` is True then load this type of
audio metadata.
**sample_rate** ([int](https://docs.python.org/3/library/functions.html#int)) – The requested sample frequency in frames per
second. If it is set to 0 then no resampling is performed. (default: 0)
**resampling_quality** – (sinc-fastest|sinc-medium|sinc-best|zero-order-hold|linear): Chooses
the audio resampling quality if resampling is performed. (default:
sinc-fastest)
**info_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the audio metadata in, if desired. (default: ‘’)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
