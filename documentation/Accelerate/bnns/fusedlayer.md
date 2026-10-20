# BNNS.FusedLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

The base class for fused convolution-normalization and fully connected-normalization layers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class FusedLayer
```

## Topics

### Applying a Fused Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](./fusedlayer/apply%28batchsize,input,output,for%29.md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](./fusedlayer/applybackward%28batchsize,input,output,outputgradient,generatinginputgradient,generatingparametergradients%29.md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](./layer.md)
### Inherited By
- [BNNS.FusedConvolutionNormalizationLayer](./fusedconvolutionnormalizationlayer.md)
- [BNNS.FusedFullyConnectedNormalizationLayer](./fusedfullyconnectednormalizationlayer.md)
- [BNNS.FusedParametersLayer](./fusedparameterslayer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedlayer)*