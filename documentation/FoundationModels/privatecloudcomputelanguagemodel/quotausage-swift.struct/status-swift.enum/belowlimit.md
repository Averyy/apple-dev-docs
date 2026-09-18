# PrivateCloudComputeLanguageModel.QuotaUsage.Status.BelowLimit

**Framework**: Foundation Models  
**Kind**: struct

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
- [var isApproachingLimit: Bool](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/belowlimit/isapproachinglimit.md)
  A Boolean value that indicates whether usage is nearing the usage limit.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case belowLimit(PrivateCloudComputeLanguageModel.QuotaUsage.Status.BelowLimit)](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/belowlimit(_:).md)
  The model’s usage is below its usage limit.
- [case limitReached(PrivateCloudComputeLanguageModel.QuotaUsage.Status.LimitReached)](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/limitreached(_:).md)
  The model’s usage has reached its usage limit.
- [PrivateCloudComputeLanguageModel.QuotaUsage.Status.LimitReached](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/limitreached.md)
  Information about usage that has reached the usage limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/belowlimit)*