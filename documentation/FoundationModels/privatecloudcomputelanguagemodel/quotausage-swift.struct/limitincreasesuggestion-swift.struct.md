# PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An offer that a user can act on to increase their quota for a language model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct LimitIncreaseSuggestion
```

## Topics

### Presenting the suggestion
- [func show()](./limitincreasesuggestion-swift.struct/show%28%29.md)
  Presents the limit increase flow to the user.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting the quota limit
- [var isLimitReached: Bool](./islimitreached.md)
  A Boolean value that indicates whether the usage limit has been reached.
- [var limitIncreaseSuggestion: PrivateCloudComputeLanguageModel.QuotaUsage.LimitIncreaseSuggestion?](./limitincreasesuggestion-swift.property.md)
  A suggestion the user can act on to increase their quota.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/quotausage-swift.struct/limitincreasesuggestion-swift.struct)*