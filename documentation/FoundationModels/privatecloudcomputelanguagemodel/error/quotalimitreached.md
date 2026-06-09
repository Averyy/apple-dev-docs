# PrivateCloudComputeLanguageModel.Error.QuotaLimitReached

**Framework**: Foundation Models  
**Kind**: struct

Information about reaching a usage limit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct QuotaLimitReached
```

#### Overview

A [`PrivateCloudComputeLanguageModel`](privatecloudcomputelanguagemodel.md)  provides a [`LanguageModelError`](languagemodelerror.md) that you use to proactively respond to usage quota scenarios, like when a person is approaching their per-day request limit. When a person approaches or exceeds the daily quota, the framework provides a direct path for you to add system UI so the person can subscribe to iCloud+ to get more access.

For more information about quota limits, see “Handle usage limits from using PCC” in [`Adding server-side intelligence with Private Cloud Compute`](adding-server-side-intelligence-with-private-cloud-compute.md).

## Topics

### Creating a quota reached error
- [init(limitIncreaseSuggestion: PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion?, resetDate: Date?, debugDescription: String)](privatecloudcomputelanguagemodel/error/quotalimitreached/init(limitincreasesuggestion:resetdate:debugdescription:).md)
  Creates a new quota limit reached instance.
### Inspecting a quota reached error
- [var limitIncreaseSuggestion: PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion?](privatecloudcomputelanguagemodel/error/quotalimitreached/limitincreasesuggestion.md)
  A suggestion to increase the usage limit, if one exists.
- [var resetDate: Date?](privatecloudcomputelanguagemodel/error/quotalimitreached/resetdate.md)
  The date that the usage limit will reset.
### Getting the error description
- [var debugDescription: String](privatecloudcomputelanguagemodel/error/quotalimitreached/debugdescription.md)
  A debug description of the usage limit.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case quotaLimitReached(PrivateCloudComputeLanguageModel.Error.QuotaLimitReached)](privatecloudcomputelanguagemodel/error/quotalimitreached(_:).md)
  The allotted usage quota has been reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error/quotalimitreached)*