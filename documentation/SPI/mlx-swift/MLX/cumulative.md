---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cumulative"
framework: "mlx-swift/MLX"
---

# Cumulative Operations

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Operations that produce a cumulative result.

#### Overview

There are a number of functions that can produce a cumulative result.  For example:

```swift
// [0, 1, 2, 3, 4]
let array = MLXArray(0 ..< 5)

// [0, 1, 3, 6, 10]
let result = array.cumsum()
```

These are available as both methods on `MLXArray` and free functions.  They each have options to:

- perform the computation along an axis or over the flattened array
- reverse the direction of cumulative computation

## Topics

### MLXArray Methods
- [func cummax(axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/cummax%28axis,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements along the given axis.
- [func cummax(reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/cummax%28reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements over the flattened array.
- [func cummin(axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/cummin%28axis,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements along the given axis.
- [func cummin(reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/cummin%28reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements over the flattened array.
- [func cumprod(axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/cumprod%28axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements along the given axis.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func cumsum(axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/cumsum%28axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements along the given axis.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func logCumsumExp(axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/logcumsumexp%28axis,reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements along the given axis.
- [func logCumsumExp(reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/logcumsumexp%28reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements of the flattened array.
### Free Functions
- [func cummax(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements along the given axis.
- [func cummax(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements over the flattened array.
- [func cummin(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements along the given axis.
- [func cummin(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28_,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements over the flattened array.
- [func cumprod(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28_,axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements along the given axis.
- [func cumprod(MLXArray, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28_,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements over the flattened array.
- [func cumsum(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28_,axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements along the given axis.
- [func cumsum(MLXArray, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28_,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements over the flattened array.
- [func logCumsumExp(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./logcumsumexp%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements along the given axis.
- [func logCumsumExp(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./logcumsumexp%28_,reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements of the flattened array.

## See Also

### Arithmetic Operators and Functions
- [Arithmetic](./arithmetic.md)
  MLX supports a wide range of binary arithmetic operators.
- [Convolution](./convolution.md)
  Convolution operations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cumulative)*