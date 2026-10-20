# SystemLanguageModel.Availability.UnavailableReason.modelNotReady

**Framework**: Foundation Models  
**Kind**: case  
**Role**: Case

The models aren’t available on the user’s device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case modelNotReady
```

#### Discussion

Models are downloaded automatically based on factors like network status, battery level, and system load.

## See Also

### Getting the unavailable reasons
- [SystemLanguageModel.Availability.UnavailableReason.appleIntelligenceNotEnabled](./appleintelligencenotenabled.md)
  Apple Intelligence is not enabled on the system.
- [SystemLanguageModel.Availability.UnavailableReason.deviceNotEligible](./devicenoteligible.md)
  The device does not support Apple Intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/availability-swift.enum/unavailablereason/modelnotready)*