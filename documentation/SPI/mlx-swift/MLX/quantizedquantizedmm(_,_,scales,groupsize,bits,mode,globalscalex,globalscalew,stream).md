---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizedquantizedmm(_:_:scales:groupsize:bits:mode:globalscalex:globalscalew:stream:)"
framework: "mlx-swift/MLX"
---

# quantizedQuantizedMM(_:_:scales:groupSize:bits:mode:globalScaleX:globalScaleW:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.

## Declaration

```swift
func quantizedQuantizedMM(_ x: MLXArray, _ w: MLXArray, scales: MLXArray?, groupSize: Int? = nil, bits: Int? = nil, mode: QuantizationMode = .nvfp4, globalScaleX: MLXArray? = nil, globalScaleW: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

If `w` is quantized, `scales` must be provided, and `groupSize`, `bits`, and `mode` must match the parameters that were used to quantize `w`.

Notes:

- If `w` is expected to receive gradients, it must be provided in non-quantized form.
- If `x` and `w` are not quantized, their data types must be [`DType.float32`](./dtype/float32.md), [`DType.float16`](./dtype/float16.md), or [`DType.bfloat16`](./dtype/bfloat16.md).
- If `w` is quantized, it must be packed in unsigned integers.

## Parameters

- `x`: Input array
- `w`: Weight matrix.  If quantized, it is packed in unsigned integers.
- `scales`: The scales to use per `groupSize` elements of `w` if `w` is quantized
- `groupSize`: Number of elements in `x` and `w` that share a scale
- `bits`: Number of bits used to represent each element of `x` and `w`
- `mode`: The quantization mode. Default is `.affine`
- `globalScaleX`: The per-input float32 scale used for `x` with  [`QuantizationMode.nvfp4`](./quantizationmode/nvfp4.md)
- `globalScaleW`: The per-input float32 scale used for  `w` with [`QuantizationMode.nvfp4`](./quantizationmode/nvfp4.md)
- `stream`: Stream or device to evaluate on

## See Also

### Quantization
- [func quantized(MLXArray, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, stream: StreamOrDevice) -> (wq: MLXArray, scales: MLXArray, biases: MLXArray?)](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md)
  Quantize the matrix `w` using `bits` bits per element.
- [func quantizedMatmul(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmatmul%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
- [func dequantized(MLXArray, scales: MLXArray, biases: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md)
  Dequantize the matrix `w` using the provided `scales` and `biases` and the `group_size` and `bits` configuration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizedquantizedmm(_:_:scales:groupsize:bits:mode:globalscalex:globalscalew:stream:))*