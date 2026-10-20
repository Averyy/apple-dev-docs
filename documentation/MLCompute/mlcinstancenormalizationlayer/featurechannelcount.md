# featureChannelCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of feature channels.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var featureChannelCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger featureChannelCount;
```

## See Also

### Inspecting Instance Normalization Layers
- [var beta: MLCTensor?](./beta.md)
  The beta tensor.
- [var betaParameter: MLCTensorParameter?](./betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gamma: MLCTensor?](./gamma.md)
  The gamma tensor.
- [var gammaParameter: MLCTensorParameter?](./gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.
- [var mean: MLCTensor?](./mean.md)
  The running mean tensor.
- [var momentum: Float](./momentum.md)
  The momentum value for the running mean and variance computation.
- [var variance: MLCTensor?](./variance.md)
  The running variance tensor.
- [var varianceEpsilon: Float](./varianceepsilon.md)
  The variance epsilon you use for numerical stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer/featurechannelcount)*