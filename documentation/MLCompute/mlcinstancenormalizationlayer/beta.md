# beta

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The beta tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var beta: MLCTensor? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) MLCTensor * beta;
```

## See Also

### Inspecting Instance Normalization Layers
- [var betaParameter: MLCTensorParameter?](./betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var featureChannelCount: Int](./featurechannelcount.md)
  The number of feature channels.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer/beta)*