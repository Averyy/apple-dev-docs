# PrivateCloudComputeLanguageModel.Availability

**Framework**: Foundation Models  
**Kind**: enum

The availability status for a specific PCC language model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
enum Availability
```

## Topics

### Checking for availability
- [PrivateCloudComputeLanguageModel.Availability.available](privatecloudcomputelanguagemodel/availability-swift.enum/available.md)
  The system is ready for making requests.
- [case unavailable(PrivateCloudComputeLanguageModel.Availability.UnavailableReason)](privatecloudcomputelanguagemodel/availability-swift.enum/unavailable(_:).md)
  Indicates that the system isn’t ready for requests.
- [PrivateCloudComputeLanguageModel.Availability.UnavailableReason](privatecloudcomputelanguagemodel/availability-swift.enum/unavailablereason.md)
  The unavailable reason.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isAvailable: Bool](privatecloudcomputelanguagemodel/isavailable.md)
  A convenience getter to check if the system is entirely ready.
- [var availability: PrivateCloudComputeLanguageModel.Availability](privatecloudcomputelanguagemodel/availability-swift.property.md)
  The availability of the language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/availability-swift.enum)*