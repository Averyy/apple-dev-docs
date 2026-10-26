# INCarCommandsDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all the handling protocols in the car commands domain.

**Availability**:
- iOS 10.3+ - Deprecated in 13.0
- iPadOS 10.3+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Please conform to INActivateCarSignalIntentHandling, INSetCarLockStatusIntentHandling, INGetCarLockStatusIntentHandling and INGetCarPowerLevelStatusIntentHandling instead

## Declaration

```swift
protocol INCarCommandsDomainHandling : INActivateCarSignalIntentHandling, INGetCarLockStatusIntentHandling, INGetCarPowerLevelStatusIntentHandling, INSetCarLockStatusIntentHandling
```

```objc
@protocol INCarCommandsDomainHandling <INActivateCarSignalIntentHandling, INSetCarLockStatusIntentHandling, INGetCarLockStatusIntentHandling, INGetCarPowerLevelStatusIntentHandling>
```

#### Overview

The `INCarCommandsDomainHandling` protocol adopts all of the protocols used to handle car command intents. You can adopt this one protocol instead of adopting the [`INActivateCarSignalIntentHandling`](./inactivatecarsignalintenthandling.md), [`INGetCarPowerLevelStatusIntentHandling`](./ingetcarpowerlevelstatusintenthandling.md), [`INGetCarLockStatusIntentHandling`](./ingetcarlockstatusintenthandling.md), and [`INSetCarLockStatusIntentHandling`](./insetcarlockstatusintenthandling.md) protocols separately.

An object that adopts this protocol must respond to the following intents:

- [`INActivateCarSignalIntent`](./inactivatecarsignalintent.md), a request to activate an audible or visual signal from the car.
- [`INGetCarPowerLevelStatusIntent`](./ingetcarpowerlevelstatusintent.md), a request for the current charge percentage remaining (for electric cars), fuel percentage remaining (for fuel-driven cars), or distance remaining given the car’s current charge or fuel.
- [`INGetCarLockStatusIntent`](./ingetcarlockstatusintent.md), a request for the current status of the car’s locks (locked or unlocked).
- [`INSetCarLockStatusIntent`](./insetcarlockstatusintent.md), a request to lock or unlock the car.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INActivateCarSignalIntentHandling](./inactivatecarsignalintenthandling.md)
- [INGetCarLockStatusIntentHandling](./ingetcarlockstatusintenthandling.md)
- [INGetCarPowerLevelStatusIntentHandling](./ingetcarpowerlevelstatusintenthandling.md)
- [INSetCarLockStatusIntentHandling](./insetcarlockstatusintenthandling.md)
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
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarcommandsdomainhandling)*