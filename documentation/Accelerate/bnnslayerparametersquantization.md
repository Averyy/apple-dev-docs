# BNNSLayerParametersQuantization

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters of a quantization layer.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSLayerParametersQuantization
```

```c
typedef struct { ... } BNNSLayerParametersQuantization;
```

## Topics

### Initializers
- [init()](./bnnslayerparametersquantization/init%28%29.md)
  Returns a new quantization layer parameters structure.
- [init(axis_mask: Int, function: BNNSQuantizerFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, scale: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor)](./bnnslayerparametersquantization/init%28axis_mask,function,i_desc,o_desc,scale,bias%29.md)
  Returns a new quantization layer parameters structure using the supplied parameters.
### Instance Properties
- [var axis_mask: Int](./bnnslayerparametersquantization/axis_mask.md)
  A bitmask that defines the axis  to which the function applies scale and bias.
- [var function: BNNSQuantizerFunction](./bnnslayerparametersquantization/function.md)
  The quantize function.
- [var i_desc: BNNSNDArrayDescriptor](./bnnslayerparametersquantization/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./bnnslayerparametersquantization/o_desc.md)
  The descriptor of the output.
- [var scale: BNNSNDArrayDescriptor](./bnnslayerparametersquantization/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor](./bnnslayerparametersquantization/bias.md)
  The descriptor of the bias.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Quantization functions
- [static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./bnns/quantize%28batchsize,input,output,axis,scale,bias,filterparameters%29.md)
  Quantizes the input tensor and writes the result to the output tensor.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./bnns/dequantize%28batchsize,input,output,axis,scale,bias,filterparameters%29.md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [struct BNNSQuantizerFunction](./bnnsquantizerfunction.md)
  Constants that describe quantization functions.
- [func BNNSDirectApplyQuantizer(UnsafePointer<BNNSLayerParametersQuantization>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](./bnnsdirectapplyquantizer%28_,_,_,_,_%29.md)
  Applies a quantization layer directly to two input matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersquantization)*