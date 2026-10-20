# scalesGradientByFrequency

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the layer scales gradients by the inverse of the frequency of words in batch before the weight update.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var scalesGradientByFrequency: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL scalesGradientByFrequency;
```

## See Also

### Inspecting Embedding Descriptors
- [var embeddingCount: Int](./embeddingcount-77gxz.md)
  The size of the dictionary.
- [var embeddingDimension: Int](./embeddingdimension-1u9g.md)
  The dimension of embedding vectors.
- [var paddingIndex: Int?](./paddingindex-pb1e.md)
  An unsigned integer value that, if set, causes the layer to initialize the embedding vector at that index to zero.
- [var maximumNorm: Float?](./maximumnorm-17u0k.md)
  A float value that, if set, causes the layer to renormalize the selected embedding vectors to have an Lp norm less than this value.
- [var pNorm: Float?](./pnorm-8vhw1.md)
  The p of the Lp norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor/scalesgradientbyfrequency)*