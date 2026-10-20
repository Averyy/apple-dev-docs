# BNNSQuantizerFunction

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe quantization functions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSQuantizerFunction
```

```c
typedef enum { ... } BNNSQuantizerFunction;
```

## Topics

### Quantization Functions
- [init(UInt32)](./bnnsquantizerfunction/init%28_%29.md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](./bnnsquantizerfunction/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](./bnnsquantizerfunction/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSQuantizerFunctionDequantize: BNNSQuantizerFunction](./bnnsquantizerfunctiondequantize.md)
  A constant that specifes conversion to a higher precision.
- [var BNNSQuantizerFunctionQuantize: BNNSQuantizerFunction](./bnnsquantizerfunctionquantize.md)
  A constant that specifes conversion to a lower precision.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Quantization functions
- [static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./bnns/quantize%28batchsize,input,output,axis,scale,bias,filterparameters%29.md)
  Quantizes the input tensor and writes the result to the output tensor.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./bnns/dequantize%28batchsize,input,output,axis,scale,bias,filterparameters%29.md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [struct BNNSLayerParametersQuantization](./bnnslayerparametersquantization.md)
  A structure that contains the parameters of a quantization layer.
- [func BNNSDirectApplyQuantizer(UnsafePointer<BNNSLayerParametersQuantization>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](./bnnsdirectapplyquantizer%28_,_,_,_,_%29.md)
  Applies a quantization layer directly to two input matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsquantizerfunction)*