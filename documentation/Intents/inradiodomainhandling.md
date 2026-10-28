# INRadioDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the radio domain.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please conform to INSetRadioStationIntentHandling instead

## Declaration

```swift
protocol INRadioDomainHandling : INSetRadioStationIntentHandling
```

```objc
@protocol INRadioDomainHandling <INSetRadioStationIntentHandling>
```

## Overview

The [`INRadioDomainHandling`](./inradiodomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle radio-related intents in a CarPlay environment. You can adopt this protocol instead of adopting the [`INSetRadioStationIntentHandling`](./insetradiostationintenthandling.md) protocol.

An object that adopts this protocol must be able to respond to the following intent:

- [`INSetRadioStationIntent`](./insetradiostationintent.md), a request to change the audio source.

Your handler object must be prepared to resolve any parameters associated with this intent and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INSetRadioStationIntentHandling](./insetradiostationintenthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Domain-Handling Protocols
- [protocol INMessagesDomainHandling](./inmessagesdomainhandling.md)
  An interface for adopting all of the protocols in the messages domain.
- [protocol INNotebookDomainHandling](./innotebookdomainhandling.md)
  An interface for adopting all of the protocols in the lists and notes domain.
- [protocol INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)
  An interface for adopting all of the protocols in the workouts domain.
- [protocol INPaymentsDomainHandling](./inpaymentsdomainhandling.md)
  An interface for adopting all of the protocols in the payments domain.
- [protocol INCallsDomainHandling](./incallsdomainhandling.md)
  Provides a convenient way to adopt all of the protocols in the VoIP calling domain.
- [protocol INVisualCodeDomainHandling](./invisualcodedomainhandling.md)
  An interface for adopting all of the protocols in the visual codes domain.
- [protocol INPhotosDomainHandling](./inphotosdomainhandling.md)
  An interface for adopting all of the protocols in the photos domain.
- [protocol INRidesharingDomainHandling](./inridesharingdomainhandling.md)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inradiodomainhandling)*