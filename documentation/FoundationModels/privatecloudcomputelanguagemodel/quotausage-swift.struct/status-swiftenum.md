# PrivateCloudComputeLanguageModel.QuotaUsage.Status

**Framework**: Foundation Models  
**Kind**: enum

The quota status of a language model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Status
```

## Topics

### Quota status
- [case belowLimit(PrivateCloudComputeLanguageModel.QuotaUsage.Status.BelowLimit)](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/belowlimit(_:).md)
  The model’s usage is below its usage limit.
- [PrivateCloudComputeLanguageModel.QuotaUsage.Status.BelowLimit](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/belowlimit.md)
  Information about usage that hasn’t yet reached the usage limit.
- [case limitReached(PrivateCloudComputeLanguageModel.QuotaUsage.Status.LimitReached)](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/limitreached(_:).md)
  The model’s usage has reached its usage limit.
- [PrivateCloudComputeLanguageModel.QuotaUsage.Status.LimitReached](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum/limitreached.md)
  Information about usage that has reached the usage limit.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var status: PrivateCloudComputeLanguageModel.QuotaUsage.Status](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.property.md)
  The current quota status.
- [var resetDate: Date?](privatecloudcomputelanguagemodel/quotausage-swift.struct/resetdate.md)
  The date at which the quota refreshes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum)*