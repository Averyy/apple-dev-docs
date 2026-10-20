# BNNS.UnaryLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

The base class for layers that accept a single input.

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
class UnaryLayer
```

## Topics

### Applying a Unary Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](./unarylayer/apply%28batchsize,input,output%29.md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](./unarylayer/applybackward%28batchsize,input,output,outputgradient,generatinginputgradient%29.md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](./layer.md)
### Inherited By
- [BNNS.ActivationLayer](./activationlayer.md)
- [BNNS.ConvolutionLayer](./convolutionlayer.md)
- [BNNS.DropoutLayer](./dropoutlayer.md)
- [BNNS.GramLayer](./gramlayer.md)
- [BNNS.PaddingLayer](./paddinglayer.md)
- [BNNS.PermuteLayer](./permutelayer.md)
- [BNNS.ReductionLayer](./reductionlayer.md)
- [BNNS.ResizeLayer](./resizelayer.md)

## See Also

### Base Classes
- [class Layer](./layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class BinaryLayer](./binarylayer.md)
  The base class for layers that accept two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/unarylayer)*