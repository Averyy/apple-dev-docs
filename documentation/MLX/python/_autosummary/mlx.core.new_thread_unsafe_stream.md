---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.new_thread_unsafe_stream.html
---

# mlx.core.new_thread_unsafe_stream

**

- [.rst](../../_sources/python/_autosummary/mlx.core.new_thread_unsafe_stream.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.new_thread_unsafe_stream

 Table of contents 

## Contents

# mlx.core.new_thread_unsafe_stream

**new_thread_unsafe_stream(*device: Device | DeviceType*) → [Stream](stream_class.html#mlx.core.Stream)**
: Make a new stream that can be used in any thread.
Unlike [new_stream()](mlx.core.new_stream.html#mlx.core.new_stream) which can only work on the thread of creation,
streams created by this API can be passed to and evaluated anywhere, but
note that currently all nodes in a graph must be evaluated in sequence
and it is user’s responsibilty to ensure there is no race condition.

** Contents
