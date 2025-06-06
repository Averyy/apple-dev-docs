# BNNSQuantizerFunction

**Framework**: Accelerate  
**Kind**: struct

Constants that describe quantization functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSQuantizerFunction
```

## Topics

### Quantization Functions
- [init(UInt32)](bnnsquantizerfunction/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](bnnsquantizerfunction/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](bnnsquantizerfunction/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSQuantizerFunctionDequantize: BNNSQuantizerFunction](bnnsquantizerfunctiondequantize.md)
  A constant that specifes conversion to a higher precision.
- [var BNNSQuantizerFunctionQuantize: BNNSQuantizerFunction](bnnsquantizerfunctionquantize.md)
  A constant that specifes conversion to a lower precision.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/quantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Quantizes the input tensor and writes the result to the output tensor.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/dequantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [struct BNNSLayerParametersQuantization](bnnslayerparametersquantization.md)
  A structure that contains the parameters of a quantization layer.
- [func BNNSDirectApplyQuantizer(UnsafePointer<BNNSLayerParametersQuantization>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyquantizer(_:_:_:_:_:).md)
  Applies a quantization layer directly to two input matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsquantizerfunction)*