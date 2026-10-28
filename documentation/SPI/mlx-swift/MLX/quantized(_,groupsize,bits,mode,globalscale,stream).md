---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantized(_:groupsize:bits:mode:globalscale:stream:)"
framework: "mlx-swift/MLX"
---

# quantized(_:groupSize:bits:mode:globalScale:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Quantize the matrix `w` using `bits` bits per element.

## Declaration

```swift
func quantized(_ w: MLXArray, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .affine, globalScale: MLXArray? = nil, stream: StreamOrDevice = .default) -> (wq: MLXArray, scales: MLXArray, biases: MLXArray?)
```

## Mentions

- [Converting From Python](./converting-python.md)

## Return Value

A tuple containing the quantized weights (`wq`), scaling factors (`scales`), and bias values (`biases`). Note that `biases` may be nil in for some `mode`.

## Discussion

Note, every `group_size` elements in a row of `w` are quantized together. Hence, number of columns of `w` should be divisible by `group_size`. In particular, the rows of `w` are divided into groups of size `group_size` which are quantized together.

> **Note**: `quantized` currently only supports 2D inputs with dimensions which are multiples of 32

For details, please see [this documentation](https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.quantize.html)

### See Also

- [`dequantized(_:scales:biases:groupSize:bits:mode:globalScale:dtype:stream:)`](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md)
- [`quantizedMM(_:_:scales:biases:transpose:groupSize:bits:mode:stream:)`](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)

## Parameters

- `w`: Matrix to be quantized
- `groupSize`: The size of the group in `w` that shares a scale and bias. Default is `64`
- `bits`: The number of bits occupied by each element of `w` in the returned quantized matrix. Default is `4`
- `mode`: The quantization mode. Default is `.affine`
- `globalScale`: The per-input float32 scale used for  [`QuantizationMode.nvfp4`](./quantizationmode/nvfp4.md)
- `stream`: Stream or device to evaluate on

## See Also

### Quantization
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func quantizedMatmul(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmatmul%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
- [func dequantized(MLXArray, scales: MLXArray, biases: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md)
  Dequantize the matrix `w` using the provided `scales` and `biases` and the `group_size` and `bits` configuration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantized(_:groupsize:bits:mode:globalscale:stream:))*