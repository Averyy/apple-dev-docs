# INCarPlayDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the CarPlay domain.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please conform to INSetAudioSourceInCarIntentHandling, INSetClimateSettingsInCarIntentHandling, INSetDefrosterSettingsInCarIntentHandling, INSetSeatSettingsInCarIntentHandling, INSetProfileInCarIntentHandling and INSaveProfileInCarIntentHandling instead

## Declaration

```swift
protocol INCarPlayDomainHandling : INSaveProfileInCarIntentHandling, INSetAudioSourceInCarIntentHandling, INSetClimateSettingsInCarIntentHandling, INSetDefrosterSettingsInCarIntentHandling, INSetProfileInCarIntentHandling, INSetSeatSettingsInCarIntentHandling
```

```objc
@protocol INCarPlayDomainHandling <INSetAudioSourceInCarIntentHandling, INSetClimateSettingsInCarIntentHandling, INSetDefrosterSettingsInCarIntentHandling, INSetSeatSettingsInCarIntentHandling, INSetProfileInCarIntentHandling, INSaveProfileInCarIntentHandling>
```

#### Overview

The [`INCarPlayDomainHandling`](./incarplaydomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle CarPlay-related intents. When your app adopts all of the protocols associated with CarPlay, you can adopt this one protocol instead of adopting the [`INSetAudioSourceInCarIntentHandling`](./insetaudiosourceincarintenthandling.md), [`INSetClimateSettingsInCarIntentHandling`](./insetclimatesettingsincarintenthandling.md), [`INSetDefrosterSettingsInCarIntentHandling`](./insetdefrostersettingsincarintenthandling.md), [`INSetSeatSettingsInCarIntentHandling`](./insetseatsettingsincarintenthandling.md), [`INSetProfileInCarIntentHandling`](./insetprofileincarintenthandling.md), and [`INSaveProfileInCarIntentHandling`](./insaveprofileincarintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INSetAudioSourceInCarIntent`](./insetaudiosourceincarintent.md), a request to change the audio source.
- [`INSetClimateSettingsInCarIntent`](./insetclimatesettingsincarintent.md), a request to change the climate control settings.
- [`INSetDefrosterSettingsInCarIntent`](./insetdefrostersettingsincarintent.md), a request to change the defroster settings.
- [`INSetSeatSettingsInCarIntent`](./insetseatsettingsincarintent.md), a request to change the seat temperature settings.
- [`INSetProfileInCarIntent`](./insetprofileincarintent.md), a request to configure the car with the specified profile information.
- [`INSaveProfileInCarIntent`](./insaveprofileincarintent.md), a request to save the current settings to a designated profile.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INSaveProfileInCarIntentHandling](./insaveprofileincarintenthandling.md)
- [INSetAudioSourceInCarIntentHandling](./insetaudiosourceincarintenthandling.md)
- [INSetClimateSettingsInCarIntentHandling](./insetclimatesettingsincarintenthandling.md)
- [INSetDefrosterSettingsInCarIntentHandling](./insetdefrostersettingsincarintenthandling.md)
- [INSetProfileInCarIntentHandling](./insetprofileincarintenthandling.md)
- [INSetSeatSettingsInCarIntentHandling](./insetseatsettingsincarintenthandling.md)
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
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarplaydomainhandling)*