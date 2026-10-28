---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizedmm(_:_:scales:biases:transpose:groupsize:bits:mode:stream:)"
framework: "mlx-swift/MLX"
---

# quantizedMM(_:_:scales:biases:transpose:groupSize:bits:mode:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Perform the matrix multiplication with the quantized matrix `w`. The quantization uses one floating point scale and bias per `group_size` of elements. Each element in `w` takes `bits` bits and is packed in an unsigned 32 bit integer.

## Declaration

```swift
func quantizedMM(_ x: MLXArray, _ w: MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool = true, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .affine, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [`dequantized(_:scales:biases:groupSize:bits:mode:globalScale:dtype:stream:)`](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md)
- [`quantized(_:groupSize:bits:mode:globalScale:stream:)`](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md)

## Parameters

- `x`: Input array
- `w`: Quantized matrix packed in unsigned integers
- `scales`: The scales to use per `groupSize` elements of `w`
- `biases`: The biases to use per `groupSize` elements of `w`
- `transpose`: Defines whether to multiply with the transposed `w` or not, namely whether we are performing `x @ w.T` or `x @ w`. Default is `true`
- `groupSize`: The size of the group in `w` that shares a scale and bias. Default is `64`
- `bits`: The number of bits occupied by each element in `w`. Default is `4`
- `mode`: The quantization mode. Default is `.affine`
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizedmm(_:_:scales:biases:transpose:groupsize:bits:mode:stream:))*