# INVisualCodeDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the visual codes domain.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

> **Deprecated**: Please conform to INGetVisualCodeIntentHandling instead

## Declaration

```swift
protocol INVisualCodeDomainHandling : INGetVisualCodeIntentHandling
```

```objc
@protocol INVisualCodeDomainHandling <INGetVisualCodeIntentHandling>
```

## Overview

The [`INVisualCodeDomainHandling`](./invisualcodedomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle QR codes and other visual codes. You can adopt this protocol instead of adopting the [`INGetVisualCodeIntentHandling`](./ingetvisualcodeintenthandling.md) protocol.

An object that adopts this protocol must be able to respond to the following intent:

- An [`INGetVisualCodeIntent`](./ingetvisualcodeintent.md) object is a request for your app to provide a visual code.

Your handler object must be prepared to resolve any parameters associated with this intent and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INGetVisualCodeIntentHandling](./ingetvisualcodeintenthandling.md)
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
- [protocol INPhotosDomainHandling](./inphotosdomainhandling.md)
  An interface for adopting all of the protocols in the photos domain.
- [protocol INRidesharingDomainHandling](./inridesharingdomainhandling.md)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invisualcodedomainhandling)*