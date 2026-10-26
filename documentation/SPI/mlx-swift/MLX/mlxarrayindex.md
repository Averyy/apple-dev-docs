---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarrayindex"
framework: "mlx-swift/MLX"
---

# MLXArrayIndex

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

Protocol for values usable as an index with [`MLXArray`](./mlxarray.md).

## Declaration

```swift
protocol MLXArrayIndex
```

##### See Also

- [Indexing](./indexing.md)
- [`subscript(_:stream:)`](./mlxarray/subscript%28_,stream%29-375a0.md)

## Topics

### Instance Properties
- [var mlxArrayIndexOperation: MLXArrayIndexOperation](./mlxarrayindex/mlxarrayindexoperation.md)
  Provide the represeting [`MLXArrayIndexOperation`](./mlxarrayindexoperation.md)
### Type Properties
- [static var ellipsis: MLXEllipsisIndex](./mlxarrayindex/ellipsis.md)
  Implementation of the `.ellipsis` MLXArray index.
- [static var newAxis: MLXNewAxisIndex](./mlxarrayindex/newaxis.md)
  Implementation of the `.newAxis`MLXArray index.
### Type Methods
- [static func stride(from: Int?, to: Int?, by: Int?) -> MLXSlice](./mlxarrayindex/stride%28from,to,by%29.md)
  MLXArray index for general slicing.

## Relationships

### Conforming Types
- [ClosedRange](./swift/closedrange.md)
- [Int](./swift/int.md)
- [MLXArray](./mlxarray.md)
- [MLXEllipsisIndex](./mlxellipsisindex.md)
- [MLXNewAxisIndex](./mlxnewaxisindex.md)
- [MLXSlice](./mlxslice.md)
- [PartialRangeFrom](./swift/partialrangefrom.md)
- [PartialRangeThrough](./swift/partialrangethrough.md)
- [PartialRangeUpTo](./swift/partialrangeupto.md)
- [Range](./swift/range.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarrayindex)*