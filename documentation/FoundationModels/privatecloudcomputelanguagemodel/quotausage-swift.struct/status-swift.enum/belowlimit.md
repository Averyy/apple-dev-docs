# PrivateCloudComputeLanguageModel.QuotaUsage.Status.BelowLimit

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Information about usage that hasn’t yet reached the usage limit.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct BelowLimit
```

## Topics

### Getting the limit status
- [var isApproachingLimit: Bool](./belowlimit/isapproachinglimit.md)
  A Boolean value that indicates whether usage is nearing the usage limit.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Quota status
- [case belowLimit(PrivateCloudComputeLanguageModel.QuotaUsage.Status.BelowLimit)](./belowlimit%28_%29.md)
  The model’s usage is below its usage limit.
- [case limitReached(PrivateCloudComputeLanguageModel.QuotaUsage.Status.LimitReached)](./limitreached%28_%29.md)
  The model’s usage has reached its usage limit.
- [PrivateCloudComputeLanguageModel.QuotaUsage.Status.LimitReached](./limitreached.md)
  Information about usage that has reached the usage limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/belowlimit)*