# betaParameter

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The beta tensor parameter you use for optimizer updates.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var betaParameter: MLCTensorParameter? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) MLCTensorParameter * betaParameter;
```

## See Also

### Inspecting Batch Normalization Layers
- [var featureChannelCount: Int](./featurechannelcount.md)
  The number of feature channels.
- [var mean: MLCTensor](./mean.md)
  The mean tensor.
- [var variance: MLCTensor](./variance.md)
  The variance tensor.
- [var beta: MLCTensor?](./beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](./gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](./varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var momentum: Float](./momentum.md)
  The value you use for the running mean and variance computation.
- [var gammaParameter: MLCTensorParameter?](./gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcbatchnormalizationlayer/betaparameter)*