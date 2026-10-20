# weights

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The weights tensor that contains the word embedding.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var weights: MLCTensor { get }
```

```objc
@property (nonatomic, retain, readonly) MLCTensor * weights;
```

## See Also

### Inspecting Embedding Layers
- [var descriptor: MLCEmbeddingDescriptor](./descriptor.md)
  The configuration object you use to create the embedding layer.
- [var weightsParameter: MLCTensorParameter](./weightsparameter.md)
  The tensor parameter that describes the weights for the optimizer update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddinglayer/weights)*