# BNNSDirectApplyQuantizer(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a quantization layer directly to two input matrices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func BNNSDirectApplyQuantizer(_ layer_params: UnsafePointer<BNNSLayerParametersQuantization>, _ filter_params: UnsafePointer<BNNSFilterParameters>?, _ batch_size: Int, _ input_stride: Int, _ output_stride: Int) -> Int32
```

#### Discussion

Use this function, in conjunction with a [`BNNSLayerParametersQuantization`](bnnslayerparametersquantization.md), to convert tensors to different precisions. Pass the [`BNNSQuantizerFunctionQuantize`](bnnsquantizerfunctionquantize.md) quantizer function to convert a higher-precsion tensor to a lower-precision tensor. Pass [`BNNSQuantizerFunctionDequantize`](bnnsquantizerfunctiondequantize.md) to convert a lower-precsion tensor to a higher-precision tensor.

Quantization supports the following conversions:

| Source | Destination |
| --- | --- |
| `BNNSDataTypeInt32` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeFloat16` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeFloat32` | `BNNSDataTypeInt8` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeUInt8` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeInt16` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeUInt16` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeInt32` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeUInt32` |

Dequantization supports the following conversions:

| Source | Destination |
| --- | --- |
| `BNNSDataTypeInt8` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeUInt8` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeInt16` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeUInt16` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeInt32` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeUInt32` | `BNNSDataTypeInt32` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeFloat16` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `BNNSDataTypeFloat32` |

You can provide optional scale and bias that the function applies during conversion. Quantization returns `y = scale*x + bias`, and dequantization returns `y = (x-bias)/scale`.

If you supply scale and bias descriptors, they must have a vector layout and a size that matches the size of the axis that you specify. If you’re applying scale and bias to the entire tensor, scale and bias descriptors must have a size of 1.

See [`BNNSQuantizerFunctionDequantize`](bnnsquantizerfunctiondequantize.md) and [`BNNSQuantizerFunctionQuantize`](bnnsquantizerfunctionquantize.md) for examples of using this function.

## Parameters

- `layer_params`: The layer parameters.
- `filter_params`: The filter runtime parameters.
- `batch_size`: The number of input-output pairs.
- `input_stride`: The increment, in values, between inputs.
- `output_stride`: The increment, in values, between outputs.

## See Also

- [static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/quantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Quantizes the input tensor and writes the result to the output tensor.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/dequantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [struct BNNSQuantizerFunction](bnnsquantizerfunction.md)
  Constants that describe quantization functions.
- [struct BNNSLayerParametersQuantization](bnnslayerparametersquantization.md)
  A structure that contains the parameters of a quantization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplyquantizer(_:_:_:_:_:))*