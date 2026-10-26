---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/matmul(_:_:stream:)"
framework: "mlx-swift/MLX"
---

# matmul(_:_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Matrix multiplication.

## Declaration

```swift
func matmul(_ a: MLXArray, _ b: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

Perform the (possibly batched) matrix multiplication of two arrays. This function supports broadcasting for arrays with more than two dimensions.

- If the first array is 1-D then a 1 is prepended to its shape to make it a matrix. Similarly if the second array is 1-D then a 1 is appended to its shape to make it a matrix. In either case the singleton dimension is removed from the result.
- A batched matrix multiplication is performed if the arrays have more than 2 dimensions.  The matrix dimensions for the matrix product are the last two dimensions of each input.
- All but the last two dimensions of each input are broadcast with one another using standard [Numpy Style Broadcasting](./broadcasting.md).

For example:

```swift
let a = MLXArray([1, 2, 3, 4], [2, 2])
let b = MLXArray(converting: [-5.0, 37.5, 4, 7, 1, 0], [2, 3])

// produces a [2, 3] result
let r = a.matmul(b)
```

##### See Also

- [Arithmetic](./arithmetic.md)
- [`multiply(_:_:stream:)`](./multiply%28_,_,stream%29.md)
- [`addMM(_:_:_:alpha:beta:stream:)`](./addmm%28_,_,_,alpha,beta,stream%29.md)
- [`blockMaskedMM(_:_:blockSize:maskOut:maskLHS:maskRHS:stream:)`](./blockmaskedmm%28_,_,blocksize,maskout,masklhs,maskrhs,stream%29.md)
- [`matmul(_:stream:)`](./mlxarray/matmul%28_,stream%29.md)

## Parameters

- `a`: The left hand side array
- `b`: The right hand side array
- `stream`: Stream or device to evaluate on

## See Also

### Element-wise Arithmetic Free Functions
- [func abs(MLXArray, stream: StreamOrDevice) -> MLXArray](./abs%28_,stream%29.md)
  Element-wise absolute value.
- [func acos(MLXArray, stream: StreamOrDevice) -> MLXArray](./acos%28_,stream%29.md)
  Element-wise inverse cosine.
- [func acosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./acosh%28_,stream%29.md)
  Element-wise inverse hyperbolic cosine.
- [func add(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./add%28_,_,stream%29.md)
  Element-wise addition.
- [func asin(MLXArray, stream: StreamOrDevice) -> MLXArray](./asin%28_,stream%29.md)
  Element-wise inverse sine.
- [func asinh(MLXArray, stream: StreamOrDevice) -> MLXArray](./asinh%28_,stream%29.md)
  Element-wise inverse hyperbolic sine.
- [func atan(MLXArray, stream: StreamOrDevice) -> MLXArray](./atan%28_,stream%29.md)
  Element-wise inverse tangent.
- [func atanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./atanh%28_,stream%29.md)
  Element-wise inverse hyperbolic tangent.
- [func ceil(MLXArray, stream: StreamOrDevice) -> MLXArray](./ceil%28_,stream%29.md)
  Element-wise ceil.
- [func clip(MLXArray, min: some ScalarOrArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,min,max,stream%29.md)
  Clip the values of the array between the given minimum and maximum.
- [func clip(MLXArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,max,stream%29.md)
  Clip the values of the array up to the given maximum.
- [func cos(MLXArray, stream: StreamOrDevice) -> MLXArray](./cos%28_,stream%29.md)
  Element-wise cosine.
- [func cosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./cosh%28_,stream%29.md)
  Element-wise hyperbolic cosine.
- [func divide(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./divide%28_,_,stream%29.md)
  Element-wise division.
- [func erf(MLXArray, stream: StreamOrDevice) -> MLXArray](./erf%28_,stream%29.md)
  Element-wise error function.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/matmul(_:_:stream:))*