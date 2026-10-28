---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/reduction"
framework: "mlx-swift/MLX"
---

# Reduction Functions

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Reduction or aggregation functions.

## Overview

MLX has a number of functions to reduce or aggregate data in `MLXArray`. These functions typically work over one or more axes, though there are overloads where the axis can be omitted and the work occurs on the entire array.

For example:

```swift
let array = MLXArray(0 ..< 12, [4, 3])

// scalar array with the sum of all the values
let totalSum = array.sum()

// array with the sum of the colums
let columnSum = array.sum(axis: 0)
```

See also [Logical Operators](./logical.md) and [Cumulative Operations](./cumulative.md)

## Topics

### MLXArray Logical Reduction Functions
- [func all(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/all%28keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/all%28axis,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/all%28axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/any%28keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/any%28axis,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/any%28axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
### MLXArray Aggregating Reduction Functions
- [func countNonzero(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/countnonzero%28keepdims,stream%29.md)
  Count the number of non-zero elements in the array over all axes.
- [func countNonzero(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/countnonzero%28axis,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axis.
- [func countNonzero(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/countnonzero%28axes,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axes.
- [func logSumExp(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/logsumexp%28keepdims,stream%29.md)
  A `log-sum-exp` reduction over the entire array.
- [func logSumExp(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/logsumexp%28axis,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axis.
- [func logSumExp(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/logsumexp%28axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func product(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/product%28keepdims,stream%29.md)
  A `product` reduction over the entire array.
- [func product(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/product%28axis,keepdims,stream%29.md)
  A `product` reduction over the given axis.
- [func product(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/product%28axes,keepdims,stream%29.md)
  A `product` reduction over the given axes.
- [func max(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/max%28keepdims,stream%29.md)
  A `max` reduction over the entire array.
- [func max(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/max%28axis,keepdims,stream%29.md)
  A `max` reduction over the given axis.
- [func max(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/max%28axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/mean%28keepdims,stream%29.md)
  A `mean` reduction over the entire array.
- [func mean(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/mean%28axis,keepdims,stream%29.md)
  A `mean` reduction over the given axis.
- [func mean(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/mean%28axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.
- [func min(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/min%28keepdims,stream%29.md)
  A `min` reduction over the entire array.
- [func min(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/min%28axis,keepdims,stream%29.md)
  A `min` reduction over the given axis.
- [func min(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/min%28axes,keepdims,stream%29.md)
  A `min` reduction over the given axes.
- [func sum(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/sum%28keepdims,stream%29.md)
  Sum reduce the array over all axes.
- [func sum(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/sum%28axis,keepdims,stream%29.md)
  Sum reduce the array over the given axis.
- [func sum(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/sum%28axes,keepdims,stream%29.md)
  Sum reduce the array over the given axes.
- [func variance(keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/variance%28keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes
- [func variance(axis: Int, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/variance%28axis,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes
- [func variance(axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/variance%28axes,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes
### Logical Reduction Free Functions
- [func all(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axis,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axis,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
### Aggregating Reduction Free Functions
- [func countNonzero(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28_,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over all axes.
- [func countNonzero(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28_,axis,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axis.
- [func countNonzero(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28_,axes,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axes.
- [func logSumExp(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the entire array.
- [func logSumExp(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axis,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axis.
- [func logSumExp(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func product(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,keepdims,stream%29.md)
  A `product` reduction over the entire array.
- [func product(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,axis,keepdims,stream%29.md)
  A `product` reduction over the given axis.
- [func product(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,axes,keepdims,stream%29.md)
  A `product` reduction over the given axes.
- [func max(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,keepdims,stream%29.md)
  A `max` reduction over the entire array.
- [func max(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axis,keepdims,stream%29.md)
  A `max` reduction over the given axis.
- [func max(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,keepdims,stream%29.md)
  A `mean` reduction over the entire array.
- [func mean(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axis,keepdims,stream%29.md)
  A `mean` reduction over the given axis.
- [func mean(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.
- [func median(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./median%28_,keepdims,stream%29.md)
  Compute the median(s) over the full array.
- [func median(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./median%28_,axis,keepdims,stream%29.md)
  Compute the median(s) over the given axis.
- [func median(MLXArray, axes: [Int], keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./median%28_,axes,keepdims,stream%29.md)
  Compute the median(s) over the given axes.
- [func min(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28_,keepdims,stream%29.md)
  A `min` reduction over the entire array.
- [func min(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28_,axis,keepdims,stream%29.md)
  A `min` reduction over the given axis.
- [func min(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28_,axes,keepdims,stream%29.md)
  A `min` reduction over the given axes.
- [func std(MLXArray, axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./std%28_,axes,keepdims,ddof,stream%29.md)
  Compute the standard deviation(s) over the given axes.
- [func std(MLXArray, axis: Int, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./std%28_,axis,keepdims,ddof,stream%29.md)
  Compute the standard deviation over the given axis.
- [func std(MLXArray, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./std%28_,keepdims,ddof,stream%29.md)
  Compute the standard deviations over all axes.
- [func sum(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,keepdims,stream%29.md)
  Sum reduce the array over all axes.
- [func sum(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,axis,keepdims,stream%29.md)
  Sum reduce the array over the given axis.
- [func sum(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,axes,keepdims,stream%29.md)
  Sum reduce the array over the given axes.
- [func variance(MLXArray, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes
- [func variance(MLXArray, axis: Int, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,axis,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes
- [func variance(MLXArray, axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,axes,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes

## See Also

### Shapes
- [Shapes](./shapes.md)
  Shape is a term to describe the number and size of the dimensions of an N dimension (ND) array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/reduction)*