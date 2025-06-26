# BNNS.ConvolutionLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a convolution filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
class ConvolutionLayer
```

## Topics

### Creating a Convolution Layer
- [convenience init?(type: BNNS.ConvolutionType, input: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, padding: BNNS.ConvolutionPadding, activation: BNNS.ActivationFunction, groupCount: Int, stride: (x: Int, y: Int), dilationStride: (x: Int, y: Int), filterParameters: BNNSFilterParameters?)](bnns/convolutionlayer/init(type:input:weights:output:bias:padding:activation:groupcount:stride:dilationstride:filterparameters:).md)
  Returns a new convolution layer.
### Specifying a Convolution Type
- [BNNS.ConvolutionType](bnns/convolutiontype.md)
  Constants that describe convolution types.
### Specifying Convolution Padding
- [BNNS.ConvolutionPadding](bnns/convolutionpadding.md)
  Constants that describe convolution padding modes.
### Applying a Convolution Layer
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient: BNNSNDArrayDescriptor?, generatingBiasGradient: BNNSNDArrayDescriptor?) throws](bnns/convolutionlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingweightsgradient:generatingbiasgradient:).md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](bnns/unarylayer.md)
### Inherited By
- [BNNS.FullyConnectedLayer](bnns/fullyconnectedlayer.md)

## See Also

- [struct BNNSConvolutionLayerParameters](bnnsconvolutionlayerparameters.md)
  A structure containing convolution parameters.
- [func BNNSFilterCreateConvolutionLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSConvolutionLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreateconvolutionlayer(_:_:_:_:).md)
  Returns a convolution filter, initialized with input, output, layer, and filter parameters.
- [struct BNNSLayerParametersConvolution](bnnslayerparametersconvolution.md)
  A structure that contains the parameters of a convolution layer.
- [func BNNSFilterCreateLayerConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerconvolution(_:_:).md)
  Returns a new convolution layer.
- [func BNNSFilterCreateLayerTransposedConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayertransposedconvolution(_:_:).md)
  Returns a new transposed convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/convolutionlayer)*