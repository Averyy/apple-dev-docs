# INBoatReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a boat reservation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INBoatReservation
```

```objc
@interface INBoatReservation : INReservation
```

## Topics

### Creating a Boat Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, boatTrip: INBoatTrip?)](./inboatreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,boattrip%29-6q5gl.md)
  Creates a boat reservation with the specified contents and attributes.
### Getting the Boat Reservation Information
- [var boatTrip: INBoatTrip?](./inboatreservation/boattrip.md)
  Information describing a voyage.
- [class INBoatTrip](./inboattrip.md)
  The information that describes a boat trip.
- [var reservedSeat: INSeat?](./inboatreservation/reservedseat.md)
  The passenger’s seat on a boat reservation.
### Initializers
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, URL: URL?, reservedSeat: INSeat?, boatTrip: INBoatTrip?)](./inboatreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,boattrip%29-24kza.md)

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

### Travel Reservations
- [class INFlightReservation](./inflightreservation.md)
  The information that describes a flight reservation.
- [class INTrainReservation](./intrainreservation.md)
  The information that describes a train reservation.
- [class INBusReservation](./inbusreservation.md)
  The information that describes a bus reservation.
- [class INRentalCarReservation](./inrentalcarreservation.md)
  The information that describes a rental car reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboatreservation)*