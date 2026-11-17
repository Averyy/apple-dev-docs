# SystemLanguageModel.Availability

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

The availability status for a specific system language model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@frozen
enum Availability
```

## Overview

> **See Also**: [`availability`](./availability-swift.property.md)

## Topics

### Checking for availability
- [SystemLanguageModel.Availability.available](./availability-swift.enum/available.md)
  The system is ready to make requests.
- [case unavailable(SystemLanguageModel.Availability.UnavailableReason)](./availability-swift.enum/unavailable%28_%29.md)
  The system isn’t ready for requests.
- [SystemLanguageModel.Availability.UnavailableReason](./availability-swift.enum/unavailablereason.md)
  The reason the system language model is unavailable.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking model availability
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the system is entirely ready.
- [var availability: SystemLanguageModel.Availability](./availability-swift.property.md)
  The availability of the language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/availability-swift.enum)*