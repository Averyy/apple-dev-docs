# descriptorWithEmbeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a new embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) descriptorWithEmbeddingCount:(NSNumber *) embeddingCount embeddingDimension:(NSNumber *) embeddingDimension paddingIndex:(NSNumber *) paddingIndex maximumNorm:(NSNumber *) maximumNorm pNorm:(NSNumber *) pNorm scalesGradientByFrequency:(BOOL) scalesGradientByFrequency;
```

#### Return Value

An embedding descriptor.

## Parameters

- `embeddingCount`: The size of the dictionary.
- `embeddingDimension`: The dimension of embedding vectors.
- `paddingIndex`: An unsigned integer value. If set, the layer initializes the embedding vector at that index to zero, and won’t update the vector in the gradient pass. The default value is `nil`.
- `maximumNorm`: A float value. If set, the layer renormalizes the selected embedding vectors in the forward pass only to have an Lp norm less than this value. The default value is `nil`.
- `pNorm`: A float value that specifies the p of the Lp norm. The default value is `2.0`.
- `scalesGradientByFrequency`: A Boolean value that indicates whether you scale the gradients by the inverse of the frequency of words in batch before the weight update. The default value is `NO`.

## See Also

### Creating Embedding Descriptors
- [+ descriptorWithEmbeddingCount:embeddingDimension:](./descriptorwithembeddingcount_embeddingdimension_.md)
  Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/descriptorwithembeddingcount:embeddingdimension:paddingindex:maximumnorm:pnorm:scalesgradientbyfrequency:)*