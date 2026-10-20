# PrivateCloudComputeLanguageModel.Availability.UnavailableReason

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

The reason the model is unavailable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum UnavailableReason
```

## Topics

### Getting the unavailable reasons
- [PrivateCloudComputeLanguageModel.Availability.UnavailableReason.deviceNotEligible](./unavailablereason/devicenoteligible.md)
  The device does not support Apple Intelligence.
- [PrivateCloudComputeLanguageModel.Availability.UnavailableReason.systemNotReady](./unavailablereason/systemnotready.md)
  The system is not yet ready to serve PCC requests.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Checking for availability
- [PrivateCloudComputeLanguageModel.Availability.available](./available.md)
  The system is ready to make requests.
- [case unavailable(PrivateCloudComputeLanguageModel.Availability.UnavailableReason)](./unavailable%28_%29.md)
  The system isn’t ready for requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/availability-swift.enum/unavailablereason)*