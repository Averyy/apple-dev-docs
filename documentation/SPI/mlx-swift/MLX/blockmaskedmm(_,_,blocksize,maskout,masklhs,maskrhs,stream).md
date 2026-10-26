---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/blockmaskedmm(_:_:blocksize:maskout:masklhs:maskrhs:stream:)"
framework: "mlx-swift/MLX"
---

# blockMaskedMM(_:_:blockSize:maskOut:maskLHS:maskRHS:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Matrix multiplication with block masking.

## Declaration

```swift
func blockMaskedMM(_ a: MLXArray, _ b: MLXArray, blockSize: Int = 64, maskOut: MLXArray? = nil, maskLHS: MLXArray? = nil, maskRHS: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Perform the (possibly batched) matrix multiplication of two arrays and with blocks of size `blockSize x blockSize` optionally masked out.

Assuming `a` with shape (…, `M`, `K`) and b with shape (…, `K`, `N`)

- `maskLHS` must have shape (…, ceil(`M` / `blockSize`), ceil(`K` / `blockSize`))
- `maskRHS` must have shape (…, ceil(`K` / `blockSize`), ceil(`N` / `blockSize`))
- `maskOut` must have shape (…, ceil(`M` / `blockSize`), ceil(`N` / `blockSize`))

> **Note**: Only `block_size=64` and `block_size=32` are currently supported

##### See Also

- [Arithmetic](./arithmetic.md)
- [`multiply(_:_:stream:)`](./multiply%28_,_,stream%29.md)
- [`addMM(_:_:_:alpha:beta:stream:)`](./addmm%28_,_,_,alpha,beta,stream%29.md)
- [`matmul(_:stream:)`](./mlxarray/matmul%28_,stream%29.md)
- [`matmul(_:_:stream:)`](./matmul%28_,_,stream%29.md)

## Parameters

- `a`: Input array
- `b`: Input array
- `blockSize`: Size of blocks to be masked. Must be `32` or `64`
- `maskOut`: Boolean mask for output
- `maskLHS`: Boolean mask for a
- `maskRHS`: Boolean mask for b
- `stream`: Stream or device to evaluate on

## See Also

### Vector, Matrix, and Tensor Products
- [func matmul(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/matmul%28_,stream%29.md)
  Matrix multiplication.
- [func matmul(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./matmul%28_,_,stream%29.md)
  Matrix multiplication.
- [func gatherMM(MLXArray, MLXArray, lhsIndices: MLXArray?, rhsIndices: MLXArray?, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gathermm%28_,_,lhsindices,rhsindices,sortedindices,stream%29.md)
  Matrix multiplication with matrix-level gather.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/blockmaskedmm(_:_:blocksize:maskout:masklhs:maskrhs:stream:))*