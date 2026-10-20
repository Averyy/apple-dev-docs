# BNNS.NormalizationType.layer(normalizationAxis:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

Layer normalization.

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
case layer(normalizationAxis: Int)
```

## See Also

### Normalization Types
- [case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](./batch%28movingmean,movingvariance%29.md)
  Batch normalization with optional moving averages.
- [BNNS.NormalizationType.group(groupCount:)](./group%28groupcount%29.md)
  Group normalization.
- [case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](./instance%28movingmean,movingvariance%29.md)
  Instance normalization with optional moving averages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype/layer(normalizationaxis:))*