---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.average_gradients.html
---

# mlx.nn.average_gradients

```python
average_gradients(gradients: Any, group: Group | None = None, all_reduce_size: int = 33554432, communication_stream: Stream | None = None)
```

Average the gradients across the distributed processes in the passed group.

This helper enables concatenating several gradients of small arrays to one
big all reduce call for better networking performance.

**Parameters:**

- **gradients** (*Any*) – The Python tree containing the gradients (it should
have the same structure across processes)
- **group** (*Optional*[[Group](mlx.core.distributed.Group.md#mlx.core.distributed.Group)]) – The group of processes to
average the gradients. If set to `None` the global group is used.
Default: `None`.
- **all_reduce_size** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Group arrays until their size in bytes exceeds
this number. Perform one communication step per group of arrays. If
less or equal to 0 array grouping is disabled. Default: `32MiB`.
- **communication_stream** (*Optional*[[Stream](stream_class.md#mlx.core.Stream)]) – The stream to use
for the communication. If unspecified the default communication
stream is used which can vary by back-end. Default: `None`.
