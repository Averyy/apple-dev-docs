# gamma

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The gamma tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var gamma: MLCTensor? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) MLCTensor * gamma;
```

## See Also

### Inspecting Group Normalization Layers
- [var featureChannelCount: Int](./featurechannelcount.md)
  The number of feature channels.
- [var groupCount: Int](./groupcount.md)
  The number of groups into which you separate the channels.
- [var beta: MLCTensor?](./beta.md)
  The beta tensor.
- [var varianceEpsilon: Float](./varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var betaParameter: MLCTensorParameter?](./betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](./gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgroupnormalizationlayer/gamma)*