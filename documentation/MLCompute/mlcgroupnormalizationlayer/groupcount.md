# groupCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of groups into which you separate the channels.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var groupCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger groupCount;
```

## See Also

### Inspecting Group Normalization Layers
- [var featureChannelCount: Int](./featurechannelcount.md)
  The number of feature channels.
- [var beta: MLCTensor?](./beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](./gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](./varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var betaParameter: MLCTensorParameter?](./betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](./gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgroupnormalizationlayer/groupcount)*