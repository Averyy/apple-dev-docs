# MLCMultiheadAttentionLayer

**Framework**: ML Compute  
**Kind**: class

A multihead, scaled dot-product attention layer that attends to one or more entries in the input key-value pairs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCMultiheadAttentionLayer
```

#### Overview

The dimensions of projections are as follows:

``

## Topics

### Creating Multi-Head Attention Layers
- [convenience init?(descriptor: MLCMultiheadAttentionDescriptor, weights: [MLCTensor], biases: [MLCTensor]?, attentionBiases: [MLCTensor]?)](mlcmultiheadattentionlayer/init(descriptor:weights:biases:attentionbiases:).md)
  Creates a multi-head attention layer with the descriptor, weights, and biases you specify.
- [class MLCMultiheadAttentionDescriptor](mlcmultiheadattentiondescriptor.md)
  A configuration object you use to create a multi-head attention layer.
### Inspecting Multi-Head Attention Layers
- [var descriptor: MLCMultiheadAttentionDescriptor](mlcmultiheadattentionlayer/descriptor.md)
  The configuration object you use to create the multi-head attention layer.
- [var weights: [MLCTensor]](mlcmultiheadattentionlayer/weights.md)
  The array of weights you use for query, key, value, and output projections.
- [var biases: [MLCTensor]?](mlcmultiheadattentionlayer/biases.md)
  The array of biases you use for query, key, value, and output projections.
- [var attentionBiases: [MLCTensor]?](mlcmultiheadattentionlayer/attentionbiases.md)
  The array of attention biases you use for key and value.
- [var weightsParameters: [MLCTensorParameter]](mlcmultiheadattentionlayer/weightsparameters.md)
  The array of weights tensor parameters you use for optimizer updates.
- [var biasesParameters: [MLCTensorParameter]?](mlcmultiheadattentionlayer/biasesparameters.md)
  The array of biases tensor parameters you use for optimizer updates.

## Relationships

### Inherits From
- [MLCLayer](mlclayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCActivationLayer](mlcactivationlayer.md)
  A layer that applies an activation function to the source tensor and produces an output.
- [class MLCSoftmaxLayer](mlcsoftmaxlayer.md)
  A layer that outputs a probability distribution as attention weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentionlayer)*