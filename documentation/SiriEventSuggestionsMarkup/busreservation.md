# BusReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A reservation for bus travel.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object BusReservation
```

## Topics

### Defining a Bus Reservation
- [object BusTrip](bustrip.md)
  Location and scheduling information for a bus trip.
- [object BusStation](busstation.md)
  The name and location of a bus station.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `reservationFor` (BusTrip) *(required)*: Details about the bus trip.
- `reservationId` (reservationId) *(required)*: A unique identifier for the reservation, consistent in all markup.
- `reservationStatus` (reservationStatus) *(required)*: The reservation’s current status.
- `reservedTicket` (Ticket): Details about the passenger’s ticket.
- `underName` (Person) *(required)*: The passenger, or the primary passenger of a multiperson reservation if the provider doesn’t require a name for each passenger.
- `broker` (Organization): An intermediary booking service.
- `url` (URL): A webpage the user can access to view reservation details.

## See Also

- [object FlightReservation](flightreservation.md)
  An airplane flight reservation.
- [object TrainReservation](trainreservation.md)
  A reservation for train travel.
- [object BoatReservation](boatreservation.md)
  A reservation for boat travel.
- [object RentalCarReservation](rentalcarreservation.md)
  A reservation to rent a car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/busreservation)*