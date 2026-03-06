# BoatReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A reservation for boat travel.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object BoatReservation
```

## Topics

### Defining a Boat Reservation
- [object BoatTrip](boattrip.md)
  Location and scheduling information for a boat trip.
- [object BoatTerminal](boatterminal.md)
  The name and location of a boat terminal.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `reservationFor` (BoatTrip) *(required)*: Details about the boat trip.
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
- [object BusReservation](busreservation.md)
  A reservation for bus travel.
- [object RentalCarReservation](rentalcarreservation.md)
  A reservation to rent a car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/boatreservation)*