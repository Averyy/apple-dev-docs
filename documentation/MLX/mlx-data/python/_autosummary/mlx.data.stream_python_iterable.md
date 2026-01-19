---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.stream_python_iterable.html
---

# mlx.data.stream_python_iterable

**

- [.rst](../../_sources/python/_autosummary/mlx.data.stream_python_iterable.rst)
- **

.pdf

**

# mlx.data.stream_python_iterable

 Table of contents 

## Contents

# mlx.data.stream_python_iterable

**mlx.data.stream_python_iterable(*iterable_factory: function*) → mlx.data._c.Stream**
: Stream samples from a python iterable.
This method allows to make an MLX data stream from any python iterable
of samples.
import mlx.data as dx

# We cannot make such a buffer as it would require more than 40GB of
# memory just to hold the integers.
dset = dx.stream_python_iterable(lambda: (dict(x=i) for i in range(10**10)))
print(next(dset)) # {'x': 0}
print(next(dset)) # {'x': 1}
dset.reset()
print(next(dset)) # {'x': 0}
print(next(dset)) # {'x': 1}

evens = dset.sample_transform(lambda s: s if s["x"] % 2 == 0 else dict())
print(next(evens)) # {'x': 2}
print(next(evens)) # {'x': 4}

Note
This function does not take the iterable directly but instead a
function that returns an iterable. This allows us to reset the
stream and restart the iteration.

Parameters:
**iterable_factory** (*callable*) – A function that returns a python
iterable object.

** Contents
