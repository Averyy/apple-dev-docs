# init(featureChannelCount:groupCount:beta:gamma:varianceEpsilon:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a group normalization layer with the number of feature channels and groups, beta and gamma tensors, and variance epsilon you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(featureChannelCount: Int, groupCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)
```

```objc
+ (instancetype) layerWithFeatureChannelCount:(NSUInteger) featureChannelCount groupCount:(NSUInteger) groupCount beta:(MLCTensor *) beta gamma:(MLCTensor *) gamma varianceEpsilon:(float) varianceEpsilon;
```

## Parameters

- `featureChannelCount`: The number of feature channels.
- `groupCount`: The number of groups into which you separate the channels.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgroupnormalizationlayer/init(featurechannelcount:groupcount:beta:gamma:varianceepsilon:))*