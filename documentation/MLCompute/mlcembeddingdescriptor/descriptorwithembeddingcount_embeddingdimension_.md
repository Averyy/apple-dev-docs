# descriptorWithEmbeddingCount:embeddingDimension:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) descriptorWithEmbeddingCount:(NSNumber *) embeddingCount embeddingDimension:(NSNumber *) embeddingDimension;
```

## Return Value

An embedding descriptor.

## Parameters

- `embeddingCount`: The size of the dictionary.
- `embeddingDimension`: The dimension of embedding vectors.

## See Also

### Creating Embedding Descriptors
- [+ descriptorWithEmbeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:](./descriptorwithembeddingcount_embeddingdimension_paddingindex_maximumnorm_pnorm_scalesgradientbyfrequency_.md)
  Creates a new embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/descriptorwithembeddingcount:embeddingdimension:)*