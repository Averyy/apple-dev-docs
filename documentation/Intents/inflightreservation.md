# INFlightReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a flight reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INFlightReservation
```

```objc
@interface INFlightReservation : INReservation
```

## Topics

### Creating a Flight Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, flight: INFlight)](./inflightreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,flight%29-4b34z.md)
  Creates a flight reservation with the specified contents and attributes.
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservedSeat: INSeat?, flight: INFlight)](./inflightreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,reservedseat,flight%29.md)
  Creates a new flight reservation with the specified contents and attributes.
### Getting the Flight Reservation Information
- [var flight: INFlight](./inflightreservation/flight.md)
  The flight information associated with the reservation.
- [class INFlight](./inflight.md)
  The information that describes a flight.
- [class INAirline](./inairline.md)
  The information that describes an airline.
- [class INAirport](./inairport.md)
  The information that describes an airport.
- [class INAirportGate](./inairportgate.md)
  The information that describes an arrival or departure gate for a flight.
- [var reservedSeat: INSeat?](./inflightreservation/reservedseat.md)
  The user’s seat for the flight.
### Initializers
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, URL: URL?, reservedSeat: INSeat?, flight: INFlight)](./inflightreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,flight%29-83jzi.md)

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
- [class INTrainReservation](./intrainreservation.md)
  The information that describes a train reservation.
- [class INBoatReservation](./inboatreservation.md)
  The information that describes a boat reservation.
- [class INBusReservation](./inbusreservation.md)
  The information that describes a bus reservation.
- [class INRentalCarReservation](./inrentalcarreservation.md)
  The information that describes a rental car reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflightreservation)*