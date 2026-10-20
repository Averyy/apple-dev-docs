# SystemLanguageModel.Availability.UnavailableReason

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

The reason the system language model is unavailable.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum UnavailableReason
```

## Topics

### Getting the unavailable reasons
- [SystemLanguageModel.Availability.UnavailableReason.appleIntelligenceNotEnabled](./unavailablereason/appleintelligencenotenabled.md)
  Apple Intelligence is not enabled on the system.
- [SystemLanguageModel.Availability.UnavailableReason.deviceNotEligible](./unavailablereason/devicenoteligible.md)
  The device does not support Apple Intelligence.
- [SystemLanguageModel.Availability.UnavailableReason.modelNotReady](./unavailablereason/modelnotready.md)
  The models aren’t available on the user’s device.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Checking for availability
- [SystemLanguageModel.Availability.available](./available.md)
  The system is ready to make requests.
- [case unavailable(SystemLanguageModel.Availability.UnavailableReason)](./unavailable%28_%29.md)
  The system isn’t ready for requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/availability-swift.enum/unavailablereason)*