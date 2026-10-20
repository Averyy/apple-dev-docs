# init(descriptor:weights:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an embedding layer with the descriptor and word embedding weights tensor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor: MLCEmbeddingDescriptor, weights: MLCTensor)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCEmbeddingDescriptor *) descriptor weights:(MLCTensor *) weights;
```

## Parameters

- `descriptor`: An object you use to configure the embedding layer.
- `weights`: A word embedding weights tensor.

## See Also

### Creating Embedding Layers
- [class MLCEmbeddingDescriptor](../mlcembeddingdescriptor.md)
  A configuration object you use to create an embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddinglayer/init(descriptor:weights:))*