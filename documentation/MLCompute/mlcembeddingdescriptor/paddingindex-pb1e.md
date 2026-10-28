# paddingIndex

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An unsigned integer value that, if set, causes the layer to initialize the embedding vector at that index to zero.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var paddingIndex: Int? { get }
```

## Discussion

If set, the layer won’t update the embedding vector at `paddingIndex` in the gradient pass.

## See Also

### Inspecting Embedding Descriptors
- [var embeddingCount: Int](./embeddingcount-77gxz.md)
  The size of the dictionary.
- [var embeddingDimension: Int](./embeddingdimension-1u9g.md)
  The dimension of embedding vectors.
- [var maximumNorm: Float?](./maximumnorm-17u0k.md)
  A float value that, if set, causes the layer to renormalize the selected embedding vectors to have an Lp norm less than this value.
- [var pNorm: Float?](./pnorm-8vhw1.md)
  The p of the Lp norm.
- [var scalesGradientByFrequency: Bool](./scalesgradientbyfrequency.md)
  A Boolean that indicates whether the layer scales gradients by the inverse of the frequency of words in batch before the weight update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/paddingindex-pb1e)*