# SystemLanguageModel.Availability

**Framework**: Foundation Models  
**Kind**: enum

The availability status for a specific system language model.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@frozen
enum Availability
```

## Topics

### Checking for availability
- [SystemLanguageModel.Availability.available](systemlanguagemodel/availability-swift.enum/available.md)
  The system is ready for making requests.
- [case unavailable(SystemLanguageModel.Availability.UnavailableReason)](systemlanguagemodel/availability-swift.enum/unavailable(_:).md)
  Indicates that the system is not ready for requests.
- [SystemLanguageModel.Availability.UnavailableReason](systemlanguagemodel/availability-swift.enum/unavailablereason.md)
  The unavailable reason.
### Comparing availability
- [static func == (SystemLanguageModel.Availability, SystemLanguageModel.Availability) -> Bool](systemlanguagemodel/availability-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](systemlanguagemodel/availability-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isAvailable: Bool](systemlanguagemodel/isavailable.md)
  A convenience getter to check if the system is entirely ready.
- [var availability: SystemLanguageModel.Availability](systemlanguagemodel/availability-swift.property.md)
  The availability of the language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/availability-swift.enum)*