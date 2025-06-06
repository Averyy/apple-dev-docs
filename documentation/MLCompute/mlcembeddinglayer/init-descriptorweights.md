# init(descriptor:weights:)

**Framework**: ML Compute  
**Kind**: init

Creates an embedding layer with the descriptor and word embedding weights tensor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor: MLCEmbeddingDescriptor, weights: MLCTensor)
```

## Parameters

- `descriptor`: An object you use to configure the embedding layer.
- `weights`: A word embedding weights tensor.

## See Also

- [class MLCEmbeddingDescriptor](mlcembeddingdescriptor.md)
  A configuration object you use to create an embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddinglayer/init(descriptor:weights:))*