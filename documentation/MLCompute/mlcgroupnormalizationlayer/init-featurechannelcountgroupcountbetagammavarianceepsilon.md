# init(featureChannelCount:groupCount:beta:gamma:varianceEpsilon:)

**Framework**: ML Compute  
**Kind**: init

Creates a group normalization layer with the number of feature channels and groups, beta and gamma tensors, and variance epsilon you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(featureChannelCount: Int, groupCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)
```

## Parameters

- `featureChannelCount`: The number of feature channels.
- `groupCount`: The number of groups into which you separate the channels.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgroupnormalizationlayer/init(featurechannelcount:groupcount:beta:gamma:varianceepsilon:))*