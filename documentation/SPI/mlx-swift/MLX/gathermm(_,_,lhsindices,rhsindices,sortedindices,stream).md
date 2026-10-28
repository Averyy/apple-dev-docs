---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gathermm(_:_:lhsindices:rhsindices:sortedindices:stream:)"
framework: "mlx-swift/MLX"
---

# gatherMM(_:_:lhsIndices:rhsIndices:sortedIndices:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Matrix multiplication with matrix-level gather.

## Declaration

```swift
func gatherMM(_ a: MLXArray, _ b: MLXArray, lhsIndices: MLXArray? = nil, rhsIndices: MLXArray? = nil, sortedIndices: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Performs a gather of the operands with the given indices followed by a (possibly batched) matrix multiplication of two arrays.  This operation is more efficient than explicitly applying a `take` followed by a `matmul`.

The indices `lhsIndices` and `rhsIndices` contain flat indices along the batch dimensions (i.e. all but the last two dimensions) of `a` and `b` respectively.

For `a` with shape `(A1, A2, ..., AS, M, K)`, `lhsIndices` contains indices from the range `[0, A1 * A2 * ... * AS)`

For `b` with shape `(B1, B2, ..., BS, M, K)`, `rhsIndices` contains indices from the range `[0, B1 * B2 * ... * BS)`

### See Also

- [Arithmetic](./arithmetic.md)
- [`matmul(_:_:stream:)`](./matmul%28_,_,stream%29.md)

## See Also

### Vector, Matrix, and Tensor Products
- [func matmul(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/matmul%28_,stream%29.md)
  Matrix multiplication.
- [func matmul(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./matmul%28_,_,stream%29.md)
  Matrix multiplication.
- [func blockMaskedMM(MLXArray, MLXArray, blockSize: Int, maskOut: MLXArray?, maskLHS: MLXArray?, maskRHS: MLXArray?, stream: StreamOrDevice) -> MLXArray](./blockmaskedmm%28_,_,blocksize,maskout,masklhs,maskrhs,stream%29.md)
  Matrix multiplication with block masking.
- [func addMM(some ScalarOrArray, some ScalarOrArray, some ScalarOrArray, alpha: Float, beta: Float, stream: StreamOrDevice) -> MLXArray](./addmm%28_,_,_,alpha,beta,stream%29.md)
  Matrix multiplication with addition and optional scaling.
- [func quantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
  Perform the matrix multiplication with the quantized matrix `w`. The quantization uses one floating point scale and bias per `group_size` of elements. Each element in `w` takes `bits` bits and is packed in an unsigned 32 bit integer.
- [func gatherQuantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, lhsIndices: MLXArray?, rhsIndices: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gatherquantizedmm%28_,_,scales,biases,lhsindices,rhsindices,transpose,groupsize,bits,mode,sortedindices,stream%29.md)
  Perform quantized matrix multiplication with matrix-level gather.
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func segmentedMM(MLXArray, MLXArray, segments: MLXArray, stream: StreamOrDevice) -> MLXArray](./segmentedmm%28_,_,segments,stream%29.md)
  Perform a matrix multiplication but segment the inner dimension and save the result for each segment separately.
- [func inner(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./inner%28_,_,stream%29.md)
  Ordinary inner product of vectors for 1-D arrays, in higher dimensions a sum product over the last axes.
- [func outer(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./outer%28_,_,stream%29.md)
  Compute the outer product of two 1-D arrays, if the array’s passed are not 1-D a flatten op will be run beforehand.
- [func tensordot(MLXArray, MLXArray, axes: Int, stream: StreamOrDevice) -> MLXArray](./tensordot%28_,_,axes,stream%29-3qkgq.md)
  Compute tensor dot product.
- [func tensordot(MLXArray, MLXArray, axes: ((Int, Int), (Int, Int)), stream: StreamOrDevice) -> MLXArray](./tensordot%28_,_,axes,stream%29-8yqyi.md)
  Compute tensor dot product.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gathermm(_:_:lhsindices:rhsindices:sortedindices:stream:))*