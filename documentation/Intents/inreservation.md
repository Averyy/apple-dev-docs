# INReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes a reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INReservation
```

```objc
@interface INReservation : NSObject
```

## Mentions

- [Donating Reservations](../SiriKit/donating-reservations.md)

#### Overview

Don’t create instances of this class directly. Instead, use the subclass associated with the type of reservation created.

## Topics

### Describing the Reservation
- [var reservationHolderName: String?](./inreservation/reservationholdername.md)
  The reservation holder’s name.
- [var reservationNumber: String?](./inreservation/reservationnumber.md)
  The reservation number.
- [var reservationStatus: INReservationStatus](./inreservation/reservationstatus.md)
  The current status of the reservation.
- [var bookingTime: Date?](./inreservation/bookingtime.md)
  The date and time the user booked the reservation.
- [var itemReference: INSpeakableString](./inreservation/itemreference.md)
  A unique reference for the reservation.
- [var actions: [INReservationAction]?](./inreservation/actions.md)
  An array containing actions the user can perform on the reservation.
- [var url: URL?](./inreservation/url.md)
  A webpage the user can access to view reservation details.
### Initializers
- [init?(coder: NSCoder)](./inreservation/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [INBoatReservation](./inboatreservation.md)
- [INBusReservation](./inbusreservation.md)
- [INFlightReservation](./inflightreservation.md)
- [INLodgingReservation](./inlodgingreservation.md)
- [INRentalCarReservation](./inrentalcarreservation.md)
- [INRestaurantReservation](./inrestaurantreservation.md)
- [INTicketedEventReservation](./inticketedeventreservation.md)
- [INTrainReservation](./intrainreservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Common Reservation Data Objects
- [class INReservationAction](./inreservationaction.md)
  An action a user can perform that’s relevant to a reservation.
- [enum INReservationStatus](./inreservationstatus.md)
  Constants that describe the current status of the reservation.
- [class INSeat](./inseat.md)
  An object containing seat information associated with a reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation)*