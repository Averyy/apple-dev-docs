# init(embeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:)

**Framework**: ML Compute  
**Kind**: init

Creates an embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(embeddingCount: Int, embeddingDimension: Int, paddingIndex: Int?, maximumNorm: Float?, pNorm: Float?, scalesGradientByFrequency: Bool)
```

## Parameters

- `embeddingCount`: The size of the dictionary.
- `embeddingDimension`: The dimension of embedding vectors.
- `paddingIndex`: An unsigned integer value. If set, the layer initializes the embedding vector at that index to zero, and won’t update the vector in the gradient pass. The default value is  .
- `maximumNorm`: A float value. If set, the layer renormalizes the selected embedding vectors in the forward pass only to have an Lp norm less than this value. The default value is  .
- `pNorm`: A float value that specifies the p of the Lp norm. The default value is  .
- `scalesGradientByFrequency`: A Boolean value that indicates whether you scale the gradients by the inverse of the frequency of words in batch before the weight update. The default value is  .

## See Also

- [convenience init?(embeddingCount: Int, embeddingDimension: Int)](mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:).md)
  Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:paddingindex:maximumnorm:pnorm:scalesgradientbyfrequency:))*