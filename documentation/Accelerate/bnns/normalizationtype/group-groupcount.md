# BNNS.NormalizationType.group(groupCount:)

**Framework**: Accelerate  
**Kind**: case

Group normalization.

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
case group(groupCount: Int)
```

## See Also

- [case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](bnns/normalizationtype/batch(movingmean:movingvariance:).md)
  Batch normalization with optional moving averages.
- [case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](bnns/normalizationtype/instance(movingmean:movingvariance:).md)
  Instance normalization with optional moving averages.
- [BNNS.NormalizationType.layer(normalizationAxis:)](bnns/normalizationtype/layer(normalizationaxis:).md)
  Layer normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype/group(groupcount:))*