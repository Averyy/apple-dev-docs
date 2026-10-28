# INGetReservationDetailsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for details about one or more reservations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INGetReservationDetailsIntent
```

```objc
@interface INGetReservationDetailsIntent : INIntent
```

## Mentions

- [Donating Reservations](../SiriKit/donating-reservations.md)

## Overview

Create an [`INGetReservationDetailsIntent`](./ingetreservationdetailsintent.md) object when the user makes a request to see the details about one or more reservations in your app. The app creates a new [`INInteraction`](./ininteraction.md) object containing the [`INGetReservationDetailsIntent`](./ingetreservationdetailsintent.md) and [`INGetReservationDetailsIntentResponse`](./ingetreservationdetailsintentresponse.md) object and donates it to the system.

## Topics

### Creating a Get Reservation Intent
- [init(reservationContainerReference: INSpeakableString?, reservationItemReferences: [INSpeakableString]?)](./ingetreservationdetailsintent/init%28reservationcontainerreference,reservationitemreferences%29.md)
  Creates an intent that describes the reservation.
### Accessing a Reservation
- [var reservationContainerReference: INSpeakableString?](./ingetreservationdetailsintent/reservationcontainerreference.md)
  A unique identifier for the array containing the reservation objects.
- [var reservationItemReferences: [INSpeakableString]?](./ingetreservationdetailsintent/reservationitemreferences.md)
  An array of unique identifiers for previously created reservations.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Reservation Details
- [class INGetReservationDetailsIntentResponse](./ingetreservationdetailsintentresponse.md)
  Your app’s response to a request for reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintent)*