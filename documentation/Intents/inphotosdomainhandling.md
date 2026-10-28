# INPhotosDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the photos domain.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Please conform to INSearchForPhotosIntentHandling and INStartPhotoPlaybackIntentHandling instead

## Declaration

```swift
protocol INPhotosDomainHandling : INSearchForPhotosIntentHandling, INStartPhotoPlaybackIntentHandling
```

```objc
@protocol INPhotosDomainHandling <INSearchForPhotosIntentHandling, INStartPhotoPlaybackIntentHandling>
```

## Overview

The [`INPhotosDomainHandling`](./inphotosdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle photo-related intents. When your app adopts all of the protocols associated with photos, you can adopt this one protocol instead of adopting the [`INSearchForPhotosIntentHandling`](./insearchforphotosintenthandling.md) and [`INStartPhotoPlaybackIntentHandling`](./instartphotoplaybackintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INSearchForPhotosIntent`](./insearchforphotosintent.md), a request to search for a specific photo.
- [`INStartPhotoPlaybackIntent`](./instartphotoplaybackintent.md), a request to begin a slideshow of the specified photos.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INSearchForPhotosIntentHandling](./insearchforphotosintenthandling.md)
- [INStartPhotoPlaybackIntentHandling](./instartphotoplaybackintenthandling.md)
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
- [protocol INRidesharingDomainHandling](./inridesharingdomainhandling.md)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inphotosdomainhandling)*