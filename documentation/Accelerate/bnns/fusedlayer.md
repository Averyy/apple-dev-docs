# BNNS.FusedLayer

**Framework**: Accelerate  
**Kind**: class

The base class for fused convolution-normalization and fully connected-normalization layers.

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
class FusedLayer
```

## Topics

### Applying a Fused Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedlayer/apply(batchsize:input:output:for:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](bnns/fusedlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingparametergradients:).md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](bnns/layer.md)
### Inherited By
- [BNNS.FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
- [BNNS.FusedFullyConnectedNormalizationLayer](bnns/fusedfullyconnectednormalizationlayer.md)
- [BNNS.FusedParametersLayer](bnns/fusedparameterslayer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedlayer)*