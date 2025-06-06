# scalesGradientByFrequency

**Framework**: ML Compute  
**Kind**: property

A Boolean that indicates whether the layer scales gradients by the inverse of the frequency of words in batch before the weight update.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var scalesGradientByFrequency: Bool { get }
```

## See Also

- [var embeddingCount: Int](mlcembeddingdescriptor/embeddingcount-77gxz.md)
  The size of the dictionary.
- [var embeddingDimension: Int](mlcembeddingdescriptor/embeddingdimension-1u9g.md)
  The dimension of embedding vectors.
- [var paddingIndex: Int?](mlcembeddingdescriptor/paddingindex-pb1e.md)
  An unsigned integer value that, if set, causes the layer to initialize the embedding vector at that index to zero.
- [var maximumNorm: Float?](mlcembeddingdescriptor/maximumnorm-17u0k.md)
  A float value that, if set, causes the layer to renormalize the selected embedding vectors to have an Lp norm less than this value.
- [var pNorm: Float?](mlcembeddingdescriptor/pnorm-8vhw1.md)
  The p of the Lp norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/scalesgradientbyfrequency)*