# FlightReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

An airplane flight reservation.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object FlightReservation
```

## Topics

### Defining a Flight Reservation
- [object Flight](flight.md)
  Location and scheduling information for an airplane flight.
- [object Airline](airline.md)
  An airline’s name and identifier.
- [object Airport](airport.md)
  The name and location of an airport.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `reservationFor` (Flight) *(required)*: Details about the flight.
- `reservationId` (reservationId) *(required)*: A unique identifier for the reservation, consistent in all markup.
- `reservationStatus` (reservationStatus) *(required)*: The reservation’s current status.
- `reservedTicket` (Ticket): Details about the attendee’s ticketed seat.
- `underName` (Person) *(required)*: The passenger, or a primary passenger if the event provider doesn’t require a name for each passenger.
- `broker` (Organization): An intermediary booking service.
- `url` (URL): A webpage the user can access to view reservation details.

## See Also

- [object TrainReservation](trainreservation.md)
  A reservation for train travel.
- [object BusReservation](busreservation.md)
  A reservation for bus travel.
- [object BoatReservation](boatreservation.md)
  A reservation for boat travel.
- [object RentalCarReservation](rentalcarreservation.md)
  A reservation to rent a car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/flightreservation)*