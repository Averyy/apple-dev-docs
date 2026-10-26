# maximumNorm

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A float value that, if set, causes the layer to renormalize the selected embedding vectors to have an Lp norm less than this value.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, readonly) NSNumber * maximumNorm;
```

#### Discussion

Renormalization occurs in the forward pass only.

## See Also

### Inspecting Embedding Descriptors
- [embeddingCount](./embeddingcount-5vs5t.md)
  The size of the dictionary.
- [embeddingDimension](./embeddingdimension-3u8w7.md)
  The dimension of embedding vectors.
- [paddingIndex](./paddingindex-50o5o.md)
  An unsigned integer value that, if set, causes the layer to initialize the embedding vector at that index to zero.
- [pNorm](./pnorm-8mto8.md)
  The p of the Lp norm.
- [var scalesGradientByFrequency: Bool](./scalesgradientbyfrequency.md)
  A Boolean that indicates whether the layer scales gradients by the inverse of the frequency of words in batch before the weight update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/maximumnorm-4mrjj)*