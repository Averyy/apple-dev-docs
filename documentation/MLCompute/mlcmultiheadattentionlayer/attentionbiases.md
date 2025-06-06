# attentionBiases

**Framework**: ML Compute  
**Kind**: property

The array of attention biases you use for key and value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var attentionBiases: [MLCTensor]? { get }
```

## See Also

- [var descriptor: MLCMultiheadAttentionDescriptor](mlcmultiheadattentionlayer/descriptor.md)
  The configuration object you use to create the multi-head attention layer.
- [var weights: [MLCTensor]](mlcmultiheadattentionlayer/weights.md)
  The array of weights you use for query, key, value, and output projections.
- [var biases: [MLCTensor]?](mlcmultiheadattentionlayer/biases.md)
  The array of biases you use for query, key, value, and output projections.
- [var weightsParameters: [MLCTensorParameter]](mlcmultiheadattentionlayer/weightsparameters.md)
  The array of weights tensor parameters you use for optimizer updates.
- [var biasesParameters: [MLCTensorParameter]?](mlcmultiheadattentionlayer/biasesparameters.md)
  The array of biases tensor parameters you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentionlayer/attentionbiases)*