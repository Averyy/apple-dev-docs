# PrivateCloudComputeLanguageModel.Availability

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

The availability status for a specific PCC language model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
enum Availability
```

## Topics

### Checking for availability
- [PrivateCloudComputeLanguageModel.Availability.available](./availability-swift.enum/available.md)
  The system is ready to make requests.
- [case unavailable(PrivateCloudComputeLanguageModel.Availability.UnavailableReason)](./availability-swift.enum/unavailable%28_%29.md)
  The system isn’t ready for requests.
- [PrivateCloudComputeLanguageModel.Availability.UnavailableReason](./availability-swift.enum/unavailablereason.md)
  The reason the model is unavailable.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the availability
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the system is entirely ready.
- [var availability: PrivateCloudComputeLanguageModel.Availability](./availability-swift.property.md)
  The availability of the language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/availability-swift.enum)*