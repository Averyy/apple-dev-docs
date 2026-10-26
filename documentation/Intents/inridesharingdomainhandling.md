# INRidesharingDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the ride-booking domain.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Please conform to INListRideOptionsIntentHandling, INRequestRideIntentHandling, INGetRideStatusIntentHandling, INCancelRideIntentHandling and INSendRideFeedbackIntentHandling instead

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
protocol INRidesharingDomainHandling : INCancelRideIntentHandling, INGetRideStatusIntentHandling, INListRideOptionsIntentHandling, INRequestRideIntentHandling, INSendRideFeedbackIntentHandling
```

*watchOS*

```swift
protocol INRidesharingDomainHandling : INGetRideStatusIntentHandling, INListRideOptionsIntentHandling, INRequestRideIntentHandling
```

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```objc
@protocol INRidesharingDomainHandling <INListRideOptionsIntentHandling, INRequestRideIntentHandling, INGetRideStatusIntentHandling, INCancelRideIntentHandling, INSendRideFeedbackIntentHandling>
```

*watchOS*

```objc
@protocol INRidesharingDomainHandling <INListRideOptionsIntentHandling, INRequestRideIntentHandling, INGetRideStatusIntentHandling>
```

#### Overview

The [`INRidesharingDomainHandling`](./inridesharingdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle ride sharing-related intents. When your app adopts all of the protocols associated with ride sharing, you can adopt this one protocol instead of adopting the [`INListRideOptionsIntentHandling`](./inlistrideoptionsintenthandling.md), [`INRequestRideIntentHandling`](./inrequestrideintenthandling.md), [`INGetRideStatusIntentHandling`](./ingetridestatusintenthandling.md), [`INCancelRideIntentHandling`](./incancelrideintenthandling.md), and [`INSendRideFeedbackIntentHandling`](./insendridefeedbackintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INListRideOptionsIntent`](./inlistrideoptionsintent.md), a request to view the available vehicles and prices.
- [`INRequestRideIntent`](./inrequestrideintent.md), a request to book a ride.
- [`INGetRideStatusIntent`](./ingetridestatusintent.md), a request to get the status of a previously booked ride.
- [`INCancelRideIntent`](./incancelrideintent.md), a request to cancel the currently active ride.
- [`INSendRideFeedbackIntent`](./insendridefeedbackintent.md), a request to record feedback for the just-completed ride.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INCancelRideIntentHandling](./incancelrideintenthandling.md)
- [INGetRideStatusIntentHandling](./ingetridestatusintenthandling.md)
- [INListRideOptionsIntentHandling](./inlistrideoptionsintenthandling.md)
- [INRequestRideIntentHandling](./inrequestrideintenthandling.md)
- [INSendRideFeedbackIntentHandling](./insendridefeedbackintenthandling.md)
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
- [protocol INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridesharingdomainhandling)*