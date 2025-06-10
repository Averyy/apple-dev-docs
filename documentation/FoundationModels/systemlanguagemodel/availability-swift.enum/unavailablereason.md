# SystemLanguageModel.Availability.UnavailableReason

**Framework**: Foundation Models  
**Kind**: enum

The unavailable reason.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
  The model(s) aren’t available on the user’s device.
### Getting the hash value
- [var hashValue: Int](systemlanguagemodel/availability-swift.enum/unavailablereason/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](systemlanguagemodel/availability-swift.enum/unavailablereason/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing the reason
- [static func == (SystemLanguageModel.Availability.UnavailableReason, SystemLanguageModel.Availability.UnavailableReason) -> Bool](systemlanguagemodel/availability-swift.enum/unavailablereason/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](systemlanguagemodel/availability-swift.enum/unavailablereason/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SystemLanguageModel.Availability.available](systemlanguagemodel/availability-swift.enum/available.md)
  The system is ready for making requests.
- [case unavailable(SystemLanguageModel.Availability.UnavailableReason)](systemlanguagemodel/availability-swift.enum/unavailable(_:).md)
  Indicates that the system is not ready for requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/availability-swift.enum/unavailablereason)*