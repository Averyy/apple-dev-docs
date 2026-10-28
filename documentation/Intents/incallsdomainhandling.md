# INCallsDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

Provides a convenient way to adopt all of the protocols in the VoIP calling domain.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Please conform to INStartAudioCallIntentHandling, INStartVideoCallIntentHandling and INSearchCallHistoryIntentHandling instead

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
protocol INCallsDomainHandling : INSearchCallHistoryIntentHandling, INStartAudioCallIntentHandling, INStartVideoCallIntentHandling
```

*watchOS*

```swift
protocol INCallsDomainHandling : INSearchCallHistoryIntentHandling, INStartAudioCallIntentHandling
```

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```objc
@protocol INCallsDomainHandling <INStartAudioCallIntentHandling, INStartVideoCallIntentHandling, INSearchCallHistoryIntentHandling>
```

*watchOS*

```objc
@protocol INCallsDomainHandling <INStartAudioCallIntentHandling, INSearchCallHistoryIntentHandling>
```

## Overview

The [`INCallsDomainHandling`](./incallsdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle call-related intents. When your app adopts all of the protocols associated with call handling, you can adopt this one protocol instead of adopting the [`INStartAudioCallIntentHandling`](./instartaudiocallintenthandling.md), [`INStartVideoCallIntentHandling`](./instartvideocallintenthandling.md), and [`INSearchCallHistoryIntentHandling`](./insearchcallhistoryintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INSearchCallHistoryIntent`](./insearchcallhistoryintent.md), a request to search for an entry in the app’s call logs.
- [`INStartAudioCallIntent`](./instartaudiocallintent.md), a request to start an audio-only call.
- [`INStartVideoCallIntent`](./instartvideocallintent.md),  a request to start a video call.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INSearchCallHistoryIntentHandling](./insearchcallhistoryintenthandling.md)
- [INStartAudioCallIntentHandling](./instartaudiocallintenthandling.md)
- [INStartVideoCallIntentHandling](./instartvideocallintenthandling.md)
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
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallsdomainhandling)*