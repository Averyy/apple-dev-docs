# BNNS.NormalizationType.instance(movingMean:movingVariance:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

Instance normalization with optional moving averages.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)
```

## See Also

### Normalization Types
- [case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](./batch%28movingmean,movingvariance%29.md)
  Batch normalization with optional moving averages.
- [BNNS.NormalizationType.group(groupCount:)](./group%28groupcount%29.md)
  Group normalization.
- [BNNS.NormalizationType.layer(normalizationAxis:)](./layer%28normalizationaxis%29.md)
  Layer normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype/instance(movingmean:movingvariance:))*