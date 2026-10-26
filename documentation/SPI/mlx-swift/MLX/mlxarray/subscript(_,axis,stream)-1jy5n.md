---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/subscript(_:axis:stream:)-1jy5n"
framework: "mlx-swift/MLX"
---

# subscript(_:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: subscript  
**Role**: Instance Subscript

Indexing using an integer index with an axis (deprecated).

> **Deprecated**: please use subscript(.ellipsis, 3) or equivalent

## Declaration

```swift
subscript(index: Int, axis axis: Int, stream stream: StreamOrDevice = .default) -> MLXArray { get set }
```

#### Overview

This method supports a range expression with an axis, for example this python code:

```python
# python
array[..., 3]
```

This can be translated to swift as:

```swift
array[.ellipsis, 3]
```

This particular subscript operator is deprecated in favor of that, but for completeness the equivalent would be:

```swift
array[3, axis: -1]
```

##### See Also

- [Indexing](../indexing.md)

## See Also

### Subscript Functions
- [subscript(any MLXArrayIndex..., stream _: StreamOrDevice) -> MLXArray](./subscript%28_,stream%29-375a0.md)
  General array indexing.
- [subscript([any MLXArrayIndex], stream _: StreamOrDevice) -> MLXArray](./subscript%28_,stream%29-7crp3.md)
  General array indexing.
- [subscript(some RangeExpression<Int>, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28_,axis,stream%29-9txbq.md)
  Indexing using a range expression (e.g. `0 ..< 5`) with an axis (deprecated).
- [subscript(from _: Int?, to _: Int?, stride _: Int, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28from,to,stride,axis,stream%29.md)
  Indexing using a stride (deprecated).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/subscript(_:axis:stream:)-1jy5n)*