---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/subscript(_:stream:)-375a0"
framework: "mlx-swift/MLX"
---

# subscript(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: subscript  
**Role**: Instance Subscript

General array indexing.

## Declaration

```swift
subscript(indices: any MLXArrayIndex..., stream stream: StreamOrDevice = .default) -> MLXArray { get set }
```

## Overview

This implements general array indexing in the same way that the python version of MLX implements it.  This is equivalent to numpy style indexing.

```swift
// index by integer
array[1]

// index by multiple integers
array[1, 3]

// index by range expression
// python: [1:5]
array[1 ..< 5]

// full range slice
// python: [:]
array[0 ...]

// slice with stride of 2
// python: [::2]
array[.stride(by: 2)]

// ellipsis operator (consume all remaining axes)
// python: [..., 3]
array[.ellipsis, 3]

// newaxis operator (insert a new axis of size 1)
// python: [None]
array[.newAxis]

// using another MLXArray as an index
let i: MLXArray
array[i]
```

These can be combined in any way with the following restrictions:

- `.ellipsis` can only be used once in an indexing operation
- `.newAxis` cannot be used in a set operation, e.g. `array[.newAxis] = MLXArray(1)` is invalid
- the number of axes given must be equal or less than the number of axes in the source array

### See Also

- [Indexing](../indexing.md)
- [Converting From Python](../converting-python.md)
- [`ellipsis`](../mlxarrayindex/ellipsis.md)
- [`newAxis`](../mlxarrayindex/newaxis.md)
- [`stride(from:to:by:)`](../mlxarrayindex/stride%28from,to,by%29.md)
- [`at`](./at.md)

## See Also

### Subscript Functions
- [subscript([any MLXArrayIndex], stream _: StreamOrDevice) -> MLXArray](./subscript%28_,stream%29-7crp3.md)
  General array indexing.
- [subscript(Int, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28_,axis,stream%29-1jy5n.md)
  Indexing using an integer index with an axis (deprecated).
- [subscript(some RangeExpression<Int>, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28_,axis,stream%29-9txbq.md)
  Indexing using a range expression (e.g. `0 ..< 5`) with an axis (deprecated).
- [subscript(from _: Int?, to _: Int?, stride _: Int, axis _: Int, stream _: StreamOrDevice) -> MLXArray](./subscript%28from,to,stride,axis,stream%29.md)
  Indexing using a stride (deprecated).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/subscript(_:stream:)-375a0)*