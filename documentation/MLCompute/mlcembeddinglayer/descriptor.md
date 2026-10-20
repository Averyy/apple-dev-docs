# descriptor

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The configuration object you use to create the embedding layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
@NSCopying
var descriptor: MLCEmbeddingDescriptor { get }
```

```objc
@property (nonatomic, copy, readonly) MLCEmbeddingDescriptor * descriptor;
```

## See Also

### Inspecting Embedding Layers
- [var weights: MLCTensor](./weights.md)
  The weights tensor that contains the word embedding.
- [var weightsParameter: MLCTensorParameter](./weightsparameter.md)
  The tensor parameter that describes the weights for the optimizer update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddinglayer/descriptor)*