---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/subscript(from:to:stride:axis:stream:)"
framework: "mlx-swift/MLX"
---

# subscript(from:to:stride:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: subscript  
**Role**: Instance Subscript

Indexing using a stride (deprecated).

> **Deprecated**: please use subscript(.ellipsis, .stride(by: 2)) or equivalent

## Declaration

```swift
subscript(from from: Int? = nil, to to: Int? = nil, stride stride: Int, axis axis: Int = -1, stream stream: StreamOrDevice = .default) -> MLXArray { get set }
```

## Overview

This method supports strided access, similar to python:

```python
# python, access strided contents of array
evens = array[..., ::2]
```

This can be translated to swift as:

```swift
evens = array[.ellipsis, .stride(by: 2)]
```

This particular subscript operator is deprecated in favor of that, but for completeness the equivalent would be:

```swift
let evens = array[stride: 2, axis: -1]
```

### See Also

- [Indexing](../indexing.md)
- [`asStrided(_:_:strides:offset:stream:)`](../asstrided%28_,_,strides,offset,stream%29.md)

## See Also

### Subscript Functions
- [subscript(any MLXArrayIndex..., stream _: StreamOrDevice) -> MLXArray](./subscript%28_,stream%29-375a0.md)
  General array indexing.
- [subscript([any MLXArrayIndex], stream _: StreamOrDevice) -> MLXArray](./subscript%28_,stream%29-7crp3.md)
  General array indexing.
- [subscript(Int, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28_,axis,stream%29-1jy5n.md)
  Indexing using an integer index with an axis (deprecated).
- [subscript(some RangeExpression<Int>, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28_,axis,stream%29-9txbq.md)
  Indexing using a range expression (e.g. `0 ..< 5`) with an axis (deprecated).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/subscript(from:to:stride:axis:stream:))*