# init(embeddingCount:embeddingDimension:)

**Framework**: ML Compute  
**Kind**: init

Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(embeddingCount: Int, embeddingDimension: Int)
```

## Parameters

- `embeddingCount`: The size of the dictionary.
- `embeddingDimension`: The dimension of embedding vectors.

## See Also

- [convenience init?(embeddingCount: Int, embeddingDimension: Int, paddingIndex: Int?, maximumNorm: Float?, pNorm: Float?, scalesGradientByFrequency: Bool)](mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:paddingindex:maximumnorm:pnorm:scalesgradientbyfrequency:).md)
  Creates an embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:))*