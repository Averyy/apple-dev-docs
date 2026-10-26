# INBusReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a bus reservation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INBusReservation
```

```objc
@interface INBusReservation : INReservation
```

## Topics

### Creating a Bus Trip Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, busTrip: INBusTrip?)](./inbusreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,bustrip%29-4spk1.md)
  Creates a bus reservation with the specified contents and attributes.
### Getting the Bus Trip Reservation Information
- [var busTrip: INBusTrip](./inbusreservation/bustrip.md)
  Information describing a bus trip.
- [class INBusTrip](./inbustrip.md)
  Information describing a bus trip.
- [var reservedSeat: INSeat?](./inbusreservation/reservedseat.md)
  Seat information for the bus reservation.
### Initializers
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, URL: URL?, reservedSeat: INSeat?, busTrip: INBusTrip?)](./inbusreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,bustrip%29-95v54.md)

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
- [class INBoatReservation](./inboatreservation.md)
  The information that describes a boat reservation.
- [class INRentalCarReservation](./inrentalcarreservation.md)
  The information that describes a rental car reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbusreservation)*