# BNNSLayerParametersQuantization

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a quantization layer.

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
struct BNNSLayerParametersQuantization
```

## Topics

### Initializers
- [init()](bnnslayerparametersquantization/init.md)
  Returns a new quantization layer parameters structure.
- [init(axis_mask: Int, function: BNNSQuantizerFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, scale: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor)](bnnslayerparametersquantization/init(axis_mask:function:i_desc:o_desc:scale:bias:).md)
  Returns a new quantization layer parameters structure using the supplied parameters.
### Instance Properties
- [var axis_mask: Int](bnnslayerparametersquantization/axis_mask.md)
  A bitmask that defines the axis  to which the function applies scale and bias.
- [var function: BNNSQuantizerFunction](bnnslayerparametersquantization/function.md)
  The quantize function.
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersquantization/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersquantization/o_desc.md)
  The descriptor of the output.
- [var scale: BNNSNDArrayDescriptor](bnnslayerparametersquantization/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor](bnnslayerparametersquantization/bias.md)
  The descriptor of the bias.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/quantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Quantizes the input tensor and writes the result to the output tensor.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/dequantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [struct BNNSQuantizerFunction](bnnsquantizerfunction.md)
  Constants that describe quantization functions.
- [func BNNSDirectApplyQuantizer(UnsafePointer<BNNSLayerParametersQuantization>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyquantizer(_:_:_:_:_:).md)
  Applies a quantization layer directly to two input matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersquantization)*