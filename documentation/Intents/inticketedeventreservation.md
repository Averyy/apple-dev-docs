# INTicketedEventReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a ticketed event reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INTicketedEventReservation
```

```objc
@interface INTicketedEventReservation : INReservation
```

## Topics

### Creating a Ticketed Event Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, event: INTicketedEvent)](./inticketedeventreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,event%29-9i6f1.md)
  Creates a ticketed event reservation with the specified contents and attributes.
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservedSeat: INSeat?, event: INTicketedEvent)](./inticketedeventreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,reservedseat,event%29.md)
  Creates a new ticketed event reservation with the specified contents and attributes.
### Getting the Ticketed Event Reservation Information
- [var event: INTicketedEvent](./inticketedeventreservation/event.md)
  An object containing detailed information about the ticketed event.
- [class INTicketedEvent](./inticketedevent.md)
  The information that describes a ticketed event.
- [var reservedSeat: INSeat?](./inticketedeventreservation/reservedseat.md)
  The user’s assigned seat for the ticketed event.
### Initializers
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, URL: URL?, reservedSeat: INSeat?, event: INTicketedEvent)](./inticketedeventreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,event%29-7vj6l.md)

## Relationships

### Inherits From
- [INReservation](./inreservation.md)
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

### Food, Lodging, and Event Reservations
- [class INRestaurantReservation](./inrestaurantreservation.md)
  The information that describes a restaurant reservation.
- [class INLodgingReservation](./inlodgingreservation.md)
  The information that describes a lodging reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedeventreservation)*