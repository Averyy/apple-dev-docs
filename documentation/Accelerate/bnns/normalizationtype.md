# BNNS.NormalizationType

**Framework**: Accelerate  
**Kind**: enum

Constants that describe normalization types.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
enum NormalizationType
```

## Topics

### Normalization Types
- [case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](bnns/normalizationtype/batch(movingmean:movingvariance:).md)
  Batch normalization with optional moving averages.
- [BNNS.NormalizationType.group(groupCount:)](bnns/normalizationtype/group(groupcount:).md)
  Group normalization.
- [case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](bnns/normalizationtype/instance(movingmean:movingvariance:).md)
  Instance normalization with optional moving averages.
- [BNNS.NormalizationType.layer(normalizationAxis:)](bnns/normalizationtype/layer(normalizationaxis:).md)
  Layer normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype)*