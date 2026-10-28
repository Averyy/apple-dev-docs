---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarrayindexoperation"
framework: "mlx-swift/MLX"
---

# MLXArrayIndexOperation

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

MLXArray index operations.

## Declaration

```swift
enum MLXArrayIndexOperation
```

## Overview

Typically produced internally by normal index operations:

```swift
let a = MLXArray(...)

print(a[1 ..< 3, .ellipsis, 3])
```

### See Also

- [Indexing](./indexing.md)

## Topics

### Enumeration Cases
- [MLXArrayIndexOperation.array(_:)](./mlxarrayindexoperation/array%28_%29.md)
  An MLXArray index, see https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing
- [MLXArrayIndexOperation.ellipsis](./mlxarrayindexoperation/ellipsis.md)
  `...` or `Ellipsis` in python – this will expand to be full range slices of all collected axes
- [MLXArrayIndexOperation.index(_:)](./mlxarrayindexoperation/index%28_%29.md)
  A single integer index
- [MLXArrayIndexOperation.newAxis](./mlxarrayindexoperation/newaxis.md)
  `None` or `newaxis` in python
- [MLXArrayIndexOperation.slice(_:)](./mlxarrayindexoperation/slice%28_%29.md)
  A slice, e.g. from `0 ..< 3` or `.stride(by: 2)`
### Instance Properties
- [var description: String](./mlxarrayindexoperation/description.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarrayindexoperation)*