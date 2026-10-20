# BNNS.NormalizationType

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe normalization types.

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
enum NormalizationType
```

## Topics

### Normalization Types
- [case batch(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](./normalizationtype/batch%28movingmean,movingvariance%29.md)
  Batch normalization with optional moving averages.
- [BNNS.NormalizationType.group(groupCount:)](./normalizationtype/group%28groupcount%29.md)
  Group normalization.
- [case instance(movingMean: BNNSNDArrayDescriptor?, movingVariance: BNNSNDArrayDescriptor?)](./normalizationtype/instance%28movingmean,movingvariance%29.md)
  Instance normalization with optional moving averages.
- [BNNS.NormalizationType.layer(normalizationAxis:)](./normalizationtype/layer%28normalizationaxis%29.md)
  Layer normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationtype)*