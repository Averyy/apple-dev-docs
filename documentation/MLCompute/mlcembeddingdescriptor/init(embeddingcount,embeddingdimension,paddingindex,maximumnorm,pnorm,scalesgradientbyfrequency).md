# init(embeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(embeddingCount: Int, embeddingDimension: Int, paddingIndex: Int?, maximumNorm: Float?, pNorm: Float?, scalesGradientByFrequency: Bool)
```

## Parameters

- `embeddingCount`: The size of the dictionary.
- `embeddingDimension`: The dimension of embedding vectors.
- `paddingIndex`: An unsigned integer value. If set, the layer initializes the embedding vector at that index to zero, and won’t update the vector in the gradient pass. The default value is `nil`.
- `maximumNorm`: A float value. If set, the layer renormalizes the selected embedding vectors in the forward pass only to have an Lp norm less than this value. The default value is `nil`.
- `pNorm`: A float value that specifies the p of the Lp norm. The default value is `2.0`.
- `scalesGradientByFrequency`: A Boolean value that indicates whether you scale the gradients by the inverse of the frequency of words in batch before the weight update. The default value is `false`.

## See Also

### Creating Embedding Descriptors
- [convenience init?(embeddingCount: Int, embeddingDimension: Int)](./init%28embeddingcount,embeddingdimension%29.md)
  Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:paddingindex:maximumnorm:pnorm:scalesgradientbyfrequency:))*