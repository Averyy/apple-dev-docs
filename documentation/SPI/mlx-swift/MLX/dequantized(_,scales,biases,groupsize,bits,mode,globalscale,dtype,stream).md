---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/dequantized(_:scales:biases:groupsize:bits:mode:globalscale:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# dequantized(_:scales:biases:groupSize:bits:mode:globalScale:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Dequantize the matrix `w` using the provided `scales` and `biases` and the `group_size` and `bits` configuration.

## Declaration

```swift
func dequantized(_ w: MLXArray, scales: MLXArray, biases: MLXArray?, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .affine, globalScale: MLXArray? = nil, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

For details, please see [this documentation](https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.dequantize.html)

### See Also

- [`quantized(_:groupSize:bits:mode:globalScale:stream:)`](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md)
- [`quantizedMM(_:_:scales:biases:transpose:groupSize:bits:mode:stream:)`](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)

## Parameters

- `w`: The quantized weight matrix to dequantize
- `scales`: Scaling factors used during quantization. Should have shape compatible with the quantized groups
- `biases`: Bias values used during quantization. Should have shape compatible with the quantized groups
- `groupSize`: The size of each quantization group. Elements are quantized in groups of this size. Default is 64
- `bits`: The number of bits used per quantized element. Default is 4
- `mode`: The quantization mode used. Either `.affine` for standard affine quantization or `.mxfp4` for MXFP4 format. Default is `.affine`
- `globalScale`: The per-input float32 scale used for  [`QuantizationMode.nvfp4`](./quantizationmode/nvfp4.md)
- `dtype`: Data type of the output.  If not specified it will be inferred from the scales and biases.
- `stream`: Stream or device to evaluate on

## See Also

### Quantization
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func quantized(MLXArray, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, stream: StreamOrDevice) -> (wq: MLXArray, scales: MLXArray, biases: MLXArray?)](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md)
  Quantize the matrix `w` using `bits` bits per element.
- [func quantizedMatmul(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmatmul%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/dequantized(_:scales:biases:groupsize:bits:mode:globalscale:dtype:stream:))*