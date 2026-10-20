# PrivateCloudComputeLanguageModel.Error.QuotaLimitReached

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Information about reaching a usage limit.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct QuotaLimitReached
```

#### Overview

A [`PrivateCloudComputeLanguageModel`](../../privatecloudcomputelanguagemodel.md)  provides a [`LanguageModelError`](../../languagemodelerror.md) that you use to proactively respond to usage quota scenarios, like when a person is approaching their per-day request limit. When a person approaches or exceeds the daily quota, the framework provides a direct path for you to add system UI so the person can subscribe to iCloud+ to get more access.

For more information about quota limits, see “Handle usage limits from using PCC” in [Adding server-side intelligence with Private Cloud Compute](../../adding-server-side-intelligence-with-private-cloud-compute.md).

## Topics

### Creating a quota reached error
- [init(limitIncreaseSuggestion: PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion?, resetDate: Date?, debugDescription: String)](./quotalimitreached/init%28limitincreasesuggestion,resetdate,debugdescription%29.md)
  Creates a quota limit reached instance.
### Inspecting a quota reached error
- [var limitIncreaseSuggestion: PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion?](./quotalimitreached/limitincreasesuggestion.md)
  A suggestion to increase the usage limit, if one exists.
- [var resetDate: Date?](./quotalimitreached/resetdate.md)
  The date that the usage limit resets.
### Getting the error description
- [var debugDescription: String](./quotalimitreached/debugdescription.md)
  A debug description of the usage limit.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Quota usage error
- [case quotaLimitReached(PrivateCloudComputeLanguageModel.Error.QuotaLimitReached)](./quotalimitreached%28_%29.md)
  The allotted usage quota has been reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error/quotalimitreached)*