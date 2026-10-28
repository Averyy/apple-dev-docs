---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/matmul(_:stream:)"
framework: "mlx-swift/MLX"
---

# matmul(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Matrix multiplication.

## Declaration

```swift
func matmul(_ other: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

Perform the (possibly batched) matrix multiplication of two arrays. This function supports broadcasting for arrays with more than two dimensions.

- If the first array is 1-D then a 1 is prepended to its shape to make it a matrix. Similarly if the second array is 1-D then a 1 is appended to its shape to make it a matrix. In either case the singleton dimension is removed from the result.
- A batched matrix multiplication is performed if the arrays have more than 2 dimensions.  The matrix dimensions for the matrix product are the last two dimensions of each input.
- All but the last two dimensions of each input are broadcast with one another using standard [Numpy Style Broadcasting](../broadcasting.md).

For example:

```swift
let a = MLXArray([1, 2, 3, 4], [2, 2])
let b = MLXArray(converting: [-5.0, 37.5, 4, 7, 1, 0], [2, 3])

// produces a [2, 3] result
let r = a.matmul(b)
```

### See Also

- [Arithmetic](../arithmetic.md)
- [`matmul(_:_:stream:)`](../matmul%28_,_,stream%29.md)

## Parameters

- `other`: The right hand side array
- `stream`: Stream or device to evaluate on

## See Also

### Vector, Matrix, and Tensor Products
- [func matmul(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](../matmul%28_,_,stream%29.md)
  Matrix multiplication.
- [func gatherMM(MLXArray, MLXArray, lhsIndices: MLXArray?, rhsIndices: MLXArray?, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](../gathermm%28_,_,lhsindices,rhsindices,sortedindices,stream%29.md)
  Matrix multiplication with matrix-level gather.
- [func blockMaskedMM(MLXArray, MLXArray, blockSize: Int, maskOut: MLXArray?, maskLHS: MLXArray?, maskRHS: MLXArray?, stream: StreamOrDevice) -> MLXArray](../blockmaskedmm%28_,_,blocksize,maskout,masklhs,maskrhs,stream%29.md)
  Matrix multiplication with block masking.
- [func addMM(some ScalarOrArray, some ScalarOrArray, some ScalarOrArray, alpha: Float, beta: Float, stream: StreamOrDevice) -> MLXArray](../addmm%28_,_,_,alpha,beta,stream%29.md)
  Matrix multiplication with addition and optional scaling.
- [func quantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](../quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
  Perform the matrix multiplication with the quantized matrix `w`. The quantization uses one floating point scale and bias per `group_size` of elements. Each element in `w` takes `bits` bits and is packed in an unsigned 32 bit integer.
- [func gatherQuantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, lhsIndices: MLXArray?, rhsIndices: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](../gatherquantizedmm%28_,_,scales,biases,lhsindices,rhsindices,transpose,groupsize,bits,mode,sortedindices,stream%29.md)
  Perform quantized matrix multiplication with matrix-level gather.
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](../quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func segmentedMM(MLXArray, MLXArray, segments: MLXArray, stream: StreamOrDevice) -> MLXArray](../segmentedmm%28_,_,segments,stream%29.md)
  Perform a matrix multiplication but segment the inner dimension and save the result for each segment separately.
- [func inner(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](../inner%28_,_,stream%29.md)
  Ordinary inner product of vectors for 1-D arrays, in higher dimensions a sum product over the last axes.
- [func outer(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](../outer%28_,_,stream%29.md)
  Compute the outer product of two 1-D arrays, if the array’s passed are not 1-D a flatten op will be run beforehand.
- [func tensordot(MLXArray, MLXArray, axes: Int, stream: StreamOrDevice) -> MLXArray](../tensordot%28_,_,axes,stream%29-3qkgq.md)
  Compute tensor dot product.
- [func tensordot(MLXArray, MLXArray, axes: ((Int, Int), (Int, Int)), stream: StreamOrDevice) -> MLXArray](../tensordot%28_,_,axes,stream%29-8yqyi.md)
  Compute tensor dot product.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/matmul(_:stream:))*