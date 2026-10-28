---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gatherquantizedmm(_:_:scales:biases:lhsindices:rhsindices:transpose:groupsize:bits:mode:sortedindices:stream:)"
framework: "mlx-swift/MLX"
---

# gatherQuantizedMM(_:_:scales:biases:lhsIndices:rhsIndices:transpose:groupSize:bits:mode:sortedIndices:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Perform quantized matrix multiplication with matrix-level gather.

## Declaration

```swift
func gatherQuantizedMM(_ x: MLXArray, _ w: MLXArray, scales: MLXArray, biases: MLXArray?, lhsIndices: MLXArray? = nil, rhsIndices: MLXArray? = nil, transpose: Bool = true, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .affine, sortedIndices: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

This operation is the quantized equivalent to [`gatherMM(_:_:lhsIndices:rhsIndices:sortedIndices:stream:)`](./gathermm%28_,_,lhsindices,rhsindices,sortedindices,stream%29.md)

Note that `scales` and `biases` must have the same batch dimensions as `w` since they represent the same quantized matrix.

### See Also

- [Arithmetic](./arithmetic.md)
- [`quantizedMM(_:_:scales:biases:transpose:groupSize:bits:mode:stream:)`](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)

## Parameters

- `x`: The input matrix
- `w`: The quantized weight matrix to be used in the matrix multiplication
- `scales`: The scales to use per `groupSize` elements of `w`
- `biases`: The biases to use per `groupSize` elements of `w`
- `lhsIndices`: Optional indices for gathering from the left-hand side matrix
- `rhsIndices`: Optional indices for gathering from the right-hand side matrix
- `transpose`: Whether to transpose the weight matrix `w`. Default is `true`
- `groupSize`: The size of the group in `w` that shares a scale and bias. Default is `64`
- `bits`: The number of bits occupied by each element in `w`. Default is `4`
- `mode`: The quantization mode. Default is `.affine`
- `sortedIndices`: Whether the indices are sorted. Default is `false`
- `stream`: Stream or device to evaluate on

## See Also

### Vector, Matrix, and Tensor Products
- [func matmul(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/matmul%28_,stream%29.md)
  Matrix multiplication.
- [func matmul(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./matmul%28_,_,stream%29.md)
  Matrix multiplication.
- [func gatherMM(MLXArray, MLXArray, lhsIndices: MLXArray?, rhsIndices: MLXArray?, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gathermm%28_,_,lhsindices,rhsindices,sortedindices,stream%29.md)
  Matrix multiplication with matrix-level gather.
- [func blockMaskedMM(MLXArray, MLXArray, blockSize: Int, maskOut: MLXArray?, maskLHS: MLXArray?, maskRHS: MLXArray?, stream: StreamOrDevice) -> MLXArray](./blockmaskedmm%28_,_,blocksize,maskout,masklhs,maskrhs,stream%29.md)
  Matrix multiplication with block masking.
- [func addMM(some ScalarOrArray, some ScalarOrArray, some ScalarOrArray, alpha: Float, beta: Float, stream: StreamOrDevice) -> MLXArray](./addmm%28_,_,_,alpha,beta,stream%29.md)
  Matrix multiplication with addition and optional scaling.
- [func quantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
  Perform the matrix multiplication with the quantized matrix `w`. The quantization uses one floating point scale and bias per `group_size` of elements. Each element in `w` takes `bits` bits and is packed in an unsigned 32 bit integer.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gatherquantizedmm(_:_:scales:biases:lhsindices:rhsindices:transpose:groupsize:bits:mode:sortedindices:stream:))*