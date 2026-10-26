---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizedmatmul(_:_:scales:biases:transpose:groupsize:bits:mode:stream:)"
framework: "mlx-swift/MLX"
---

# quantizedMatmul(_:_:scales:biases:transpose:groupSize:bits:mode:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func quantizedMatmul(_ x: MLXArray, _ w: MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool = true, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .affine, stream: StreamOrDevice = .default) -> MLXArray
```

## See Also

### Quantization
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func quantized(MLXArray, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, stream: StreamOrDevice) -> (wq: MLXArray, scales: MLXArray, biases: MLXArray?)](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md)
  Quantize the matrix `w` using `bits` bits per element.
- [func dequantized(MLXArray, scales: MLXArray, biases: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md)
  Dequantize the matrix `w` using the provided `scales` and `biases` and the `group_size` and `bits` configuration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizedmatmul(_:_:scales:biases:transpose:groupsize:bits:mode:stream:))*