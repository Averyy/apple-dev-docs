# init(descriptor:weights:biases:attentionBiases:)

**Framework**: ML Compute  
**Kind**: init

Creates a multi-head attention layer with the descriptor, weights, and biases you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(descriptor: MLCMultiheadAttentionDescriptor, weights: [MLCTensor], biases: [MLCTensor]?, attentionBiases: [MLCTensor]?)
```

## Parameters

- `descriptor`: An object you use to configure the multi-head attention layer.
- `weights`: An array that contains the weights that correspond to query, key, value, and output projections for all heads.
- `biases`: An array that contains the biases that correspond to query, key, value, and output projections for all heads.
- `attentionBiases`: An array that contains the biases you add to the key and value, respectively.

## See Also

- [class MLCMultiheadAttentionDescriptor](mlcmultiheadattentiondescriptor.md)
  A configuration object you use to create a multi-head attention layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentionlayer/init(descriptor:weights:biases:attentionbiases:))*