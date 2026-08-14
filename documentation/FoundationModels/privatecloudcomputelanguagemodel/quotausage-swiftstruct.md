# PrivateCloudComputeLanguageModel.QuotaUsage

**Framework**: Foundation Models  
**Kind**: struct

The usage quota state for a Private Cloud Compute language model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct QuotaUsage
```

#### Overview

A quota describes the model’s per-user request budget and where the caller currently sits relative to it. Quotas are orthogonal to a model’s availability — a model can be available even after its usage limit has been reached.

## Topics

### Inspecting the quota limit
- [var isLimitReached: Bool](privatecloudcomputelanguagemodel/quotausage-swift.struct/islimitreached.md)
  A Boolean value that indicates whether the usage limit has been reached.
- [var limitIncreaseSuggestion: PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion?](privatecloudcomputelanguagemodel/quotausage-swift.struct/limitincreasesuggestion-swift.property.md)
  A suggestion the user can act on to increase their quota.
- [PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion](privatecloudcomputelanguagemodel/quotausage-swift.struct/limitincreasesuggestion-swift.struct.md)
  An offer that a user can act on to increase their quota for a language model.
### Getting the quota status
- [var status: PrivateCloudComputeLanguageModel.QuotaUsage.Status](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.property.md)
  The current quota status.
- [PrivateCloudComputeLanguageModel.QuotaUsage.Status](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum.md)
  The quota status of a language model.
- [var resetDate: Date?](privatecloudcomputelanguagemodel/quotausage-swift.struct/resetdate.md)
  The date at which the quota refreshes.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var quotaUsage: PrivateCloudComputeLanguageModel.QuotaUsage](privatecloudcomputelanguagemodel/quotausage-swift.property.md)
  The usage quota for this model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/quotausage-swift.struct)*