# init(descriptor:weights:biases:attentionBiases:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a multi-head attention layer with the descriptor, weights, and biases you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(descriptor: MLCMultiheadAttentionDescriptor, weights: [MLCTensor], biases: [MLCTensor]?, attentionBiases: [MLCTensor]?)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCMultiheadAttentionDescriptor *) descriptor weights:(NSArray<MLCTensor *> *) weights biases:(NSArray<MLCTensor *> *) biases attentionBiases:(NSArray<MLCTensor *> *) attentionBiases;
```

## Parameters

- `descriptor`: An object you use to configure the multi-head attention layer.
- `weights`: An array that contains the weights that correspond to query, key, value, and output projections for all heads.
- `biases`: An array that contains the biases that correspond to query, key, value, and output projections for all heads.
- `attentionBiases`: An array that contains the biases you add to the key and value, respectively.

## See Also

### Creating Multi-Head Attention Layers
- [class MLCMultiheadAttentionDescriptor](../mlcmultiheadattentiondescriptor.md)
  A configuration object you use to create a multi-head attention layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentionlayer/init(descriptor:weights:biases:attentionbiases:))*