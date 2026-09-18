# SystemLanguageModel.Availability.UnavailableReason

**Framework**: Foundation Models  
**Kind**: enum

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
- [SystemLanguageModel.Availability.UnavailableReason.appleIntelligenceNotEnabled](systemlanguagemodel/availability-swift.enum/unavailablereason/appleintelligencenotenabled.md)
  Apple Intelligence is not enabled on the system.
- [SystemLanguageModel.Availability.UnavailableReason.deviceNotEligible](systemlanguagemodel/availability-swift.enum/unavailablereason/devicenoteligible.md)
  The device does not support Apple Intelligence.
- [SystemLanguageModel.Availability.UnavailableReason.modelNotReady](systemlanguagemodel/availability-swift.enum/unavailablereason/modelnotready.md)
  The models aren’t available on the user’s device.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [SystemLanguageModel.Availability.available](systemlanguagemodel/availability-swift.enum/available.md)
  The system is ready to make requests.
- [case unavailable(SystemLanguageModel.Availability.UnavailableReason)](systemlanguagemodel/availability-swift.enum/unavailable(_:).md)
  The system isn’t ready for requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/availability-swift.enum/unavailablereason)*