# TrainReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A reservation for train travel.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object TrainReservation
```

## Topics

### Defining a Train Reservation
- [object TrainTrip](traintrip.md)
  Location and scheduling information for a train trip.
- [object TrainStation](trainstation.md)
  The name and location of a train station.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `reservationFor` (TrainTrip) *(required)*: Details about the train trip.
- `reservationId` (reservationId) *(required)*: A unique identifier for the reservation, consistent in all markup.
- `reservationStatus` (reservationStatus) *(required)*: The reservation’s current status.
- `reservedTicket` (Ticket): Details about the passenger’s ticket.
- `underName` (Person) *(required)*: The passenger, or the primary passenger of a multiperson reservation if the provider doesn’t require a name for each passenger.
- `broker` (Organization): An intermediary booking service.
- `url` (URL): A webpage the user can access to view reservation details.

## See Also

- [object FlightReservation](flightreservation.md)
  An airplane flight reservation.
- [object BusReservation](busreservation.md)
  A reservation for bus travel.
- [object BoatReservation](boatreservation.md)
  A reservation for boat travel.
- [object RentalCarReservation](rentalcarreservation.md)
  A reservation to rent a car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/trainreservation)*