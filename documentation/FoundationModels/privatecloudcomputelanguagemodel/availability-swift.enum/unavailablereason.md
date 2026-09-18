# PrivateCloudComputeLanguageModel.Availability.UnavailableReason

**Framework**: Foundation Models  
**Kind**: enum

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
- [PrivateCloudComputeLanguageModel.Availability.UnavailableReason.deviceNotEligible](privatecloudcomputelanguagemodel/availability-swift.enum/unavailablereason/devicenoteligible.md)
  The device does not support Apple Intelligence.
- [PrivateCloudComputeLanguageModel.Availability.UnavailableReason.systemNotReady](privatecloudcomputelanguagemodel/availability-swift.enum/unavailablereason/systemnotready.md)
  The system is not yet ready to serve PCC requests.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [PrivateCloudComputeLanguageModel.Availability.available](privatecloudcomputelanguagemodel/availability-swift.enum/available.md)
  The system is ready to make requests.
- [case unavailable(PrivateCloudComputeLanguageModel.Availability.UnavailableReason)](privatecloudcomputelanguagemodel/availability-swift.enum/unavailable(_:).md)
  The system isn’t ready for requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/availability-swift.enum/unavailablereason)*