# BNNS.NormalizationType.instance(movingMean:movingVariance:)

**Framework**: Accelerate  
**Kind**: case

Instance normalization with optional moving averages.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)
```

## See Also

- [case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](bnns/normalizationtype/batch(movingmean:movingvariance:).md)
  Batch normalization with optional moving averages.
- [BNNS.NormalizationType.group(groupCount:)](bnns/normalizationtype/group(groupcount:).md)
  Group normalization.
- [BNNS.NormalizationType.layer(normalizationAxis:)](bnns/normalizationtype/layer(normalizationaxis:).md)
  Layer normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype/instance(movingmean:movingvariance:))*