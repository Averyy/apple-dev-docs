# normalizedShape

**Framework**: ML Compute  
**Kind**: property

The shape of the axes where normalization occurs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var normalizedShape: [Int] { get }
```

#### Discussion

Define the shape of the axes in the dimensions `[w]`, `[h, w]`, or `[c, h, w]`, where `w` is width, `h` is height, and `c` is channel count.

## See Also

- [var beta: MLCTensor?](mlclayernormalizationlayer/beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](mlclayernormalizationlayer/gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](mlclayernormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var betaParameter: MLCTensorParameter?](mlclayernormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](mlclayernormalizationlayer/gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayernormalizationlayer/normalizedshape-8ujvv)*