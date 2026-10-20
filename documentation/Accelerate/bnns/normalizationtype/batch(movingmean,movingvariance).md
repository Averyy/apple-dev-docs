# BNNS.NormalizationType.batch(movingMean:movingVariance:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

Batch normalization with optional moving averages.

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
case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)
```

## See Also

### Normalization Types
- [BNNS.NormalizationType.group(groupCount:)](./group%28groupcount%29.md)
  Group normalization.
- [case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](./instance%28movingmean,movingvariance%29.md)
  Instance normalization with optional moving averages.
- [BNNS.NormalizationType.layer(normalizationAxis:)](./layer%28normalizationaxis%29.md)
  Layer normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype/batch(movingmean:movingvariance:))*