# init(embeddingCount:embeddingDimension:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(embeddingCount: Int, embeddingDimension: Int)
```

## Parameters

- `embeddingCount`: The size of the dictionary.
- `embeddingDimension`: The dimension of embedding vectors.

## See Also

### Creating Embedding Descriptors
- [convenience init?(embeddingCount: Int, embeddingDimension: Int, paddingIndex: Int?, maximumNorm: Float?, pNorm: Float?, scalesGradientByFrequency: Bool)](./init%28embeddingcount,embeddingdimension,paddingindex,maximumnorm,pnorm,scalesgradientbyfrequency%29.md)
  Creates an embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:))*