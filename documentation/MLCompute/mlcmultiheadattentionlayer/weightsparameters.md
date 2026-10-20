# weightsParameters

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The array of weights tensor parameters you use for optimizer updates.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var weightsParameters: [MLCTensorParameter] { get }
```

```objc
@property (nonatomic, retain, readonly) NSArray<MLCTensorParameter *> * weightsParameters;
```

## See Also

### Inspecting Multi-Head Attention Layers
- [var descriptor: MLCMultiheadAttentionDescriptor](./descriptor.md)
  The configuration object you use to create the multi-head attention layer.
- [var weights: [MLCTensor]](./weights.md)
  The array of weights you use for query, key, value, and output projections.
- [var biases: [MLCTensor]?](./biases.md)
  The array of biases you use for query, key, value, and output projections.
- [var attentionBiases: [MLCTensor]?](./attentionbiases.md)
  The array of attention biases you use for key and value.
- [var biasesParameters: [MLCTensorParameter]?](./biasesparameters.md)
  The array of biases tensor parameters you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentionlayer/weightsparameters)*