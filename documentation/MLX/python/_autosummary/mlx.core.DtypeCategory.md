---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.DtypeCategory.html
---

# mlx.core.DtypeCategory

```python
class DtypeCategory(*values)
```

Type to hold categories of [dtypes](mlx.core.Dtype.md#mlx.core.Dtype).

- `generic`

  - [bool_](../data_types.md#data-types)
  - `number`

    - `integer`

      - `unsignedinteger`

        - [uint8](../data_types.md#data-types)
        - [uint16](../data_types.md#data-types)
        - [uint32](../data_types.md#data-types)
        - [uint64](../data_types.md#data-types)

      - `signedinteger`

        - [int8](../data_types.md#data-types)
        - [int32](../data_types.md#data-types)
        - [int64](../data_types.md#data-types)

    - `inexact`

      - `floating`

        - [float16](../data_types.md#data-types)
        - [bfloat16](../data_types.md#data-types)
        - [float32](../data_types.md#data-types)
        - [float64](../data_types.md#data-types)

      - `complexfloating`

        - [complex64](../data_types.md#data-types)

See also [issubdtype()](mlx.core.issubdtype.md#mlx.core.issubdtype).

```python
__init__(*args, **kwds)
```

Attributes

| `complexfloating` |  |
| --- | --- |
| `floating` |  |
| `inexact` |  |
| `signedinteger` |  |
| `unsignedinteger` |  |
| `integer` |  |
| `number` |  |
| `generic` |  |
