# INWorkoutsDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the workouts domain.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Please conform to INStartWorkoutIntentHandling, INPauseWorkoutIntentHandling, INEndWorkoutIntentHandling, INCancelWorkoutIntentHandling and INResumeWorkoutIntentHandling instead

## Declaration

```swift
protocol INWorkoutsDomainHandling : INCancelWorkoutIntentHandling, INEndWorkoutIntentHandling, INPauseWorkoutIntentHandling, INResumeWorkoutIntentHandling, INStartWorkoutIntentHandling
```

```objc
@protocol INWorkoutsDomainHandling <INStartWorkoutIntentHandling, INPauseWorkoutIntentHandling, INEndWorkoutIntentHandling, INCancelWorkoutIntentHandling, INResumeWorkoutIntentHandling>
```

## Overview

The [`INWorkoutsDomainHandling`](./inworkoutsdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle workout-related intents. When your app adopts all of the protocols associated with workouts, you can adopt this one protocol instead of adopting the [`INStartWorkoutIntentHandling`](./instartworkoutintenthandling.md), [`INPauseWorkoutIntentHandling`](./inpauseworkoutintenthandling.md), [`INResumeWorkoutIntentHandling`](./inresumeworkoutintenthandling.md), [`INCancelWorkoutIntentHandling`](./incancelworkoutintenthandling.md), and [`INEndWorkoutIntentHandling`](./inendworkoutintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INStartWorkoutIntent`](./instartworkoutintent.md), a request to start a new workout.
- [`INPauseWorkoutIntent`](./inpauseworkoutintent.md), a request to pause the current workout.
- [`INResumeWorkoutIntent`](./inresumeworkoutintent.md), a request to resume a paused workout.
- [`INEndWorkoutIntent`](./inendworkoutintent.md), a request to end the active workout and save the results.
- [`INCancelWorkoutIntent`](./incancelworkoutintent.md), a request to cancel the active workout without saving the results.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INCancelWorkoutIntentHandling](./incancelworkoutintenthandling.md)
- [INEndWorkoutIntentHandling](./inendworkoutintenthandling.md)
- [INPauseWorkoutIntentHandling](./inpauseworkoutintenthandling.md)
- [INResumeWorkoutIntentHandling](./inresumeworkoutintenthandling.md)
- [INStartWorkoutIntentHandling](./instartworkoutintenthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Domain-Handling Protocols
- [protocol INMessagesDomainHandling](./inmessagesdomainhandling.md)
  An interface for adopting all of the protocols in the messages domain.
- [protocol INNotebookDomainHandling](./innotebookdomainhandling.md)
  An interface for adopting all of the protocols in the lists and notes domain.
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
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutsdomainhandling)*