# BNNS.UnaryLayer

**Framework**: Accelerate  
**Kind**: class

The base class for layers that accept a single input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
class UnaryLayer
```

## Topics

### Applying a Unary Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/unarylayer/apply(batchsize:input:output:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/unarylayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:).md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](bnns/layer.md)
### Inherited By
- [BNNS.ActivationLayer](bnns/activationlayer.md)
- [BNNS.ConvolutionLayer](bnns/convolutionlayer.md)
- [BNNS.DropoutLayer](bnns/dropoutlayer.md)
- [BNNS.GramLayer](bnns/gramlayer.md)
- [BNNS.PaddingLayer](bnns/paddinglayer.md)
- [BNNS.PermuteLayer](bnns/permutelayer.md)
- [BNNS.ReductionLayer](bnns/reductionlayer.md)
- [BNNS.ResizeLayer](bnns/resizelayer.md)

## See Also

- [class Layer](bnns/layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class BinaryLayer](bnns/binarylayer.md)
  The base class for layers that accept two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/unarylayer)*