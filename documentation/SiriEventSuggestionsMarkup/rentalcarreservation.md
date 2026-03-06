# RentalCarReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A reservation to rent a car.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object RentalCarReservation
```

## Topics

### Defining a Rental Car Reservation
- [object Car](car.md)
  A description of a rental vehicle.
- [object Brand](brand.md)
  A car brand.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `dropoffLocation` (Place) *(required)*: The place where the renter returns the car.
- `dropoffTime` (dateTimeISO8601) *(required)*: The latest time the renter may return the car.
- `pickupLocation` (Place) *(required)*: The place where the renter picks up the car.
- `pickupTime` (dateTimeISO8601) *(required)*: The earliest time the driver may pick up the car.
- `reservationFor` (Car) *(required)*: The type of vehicle to be rented.
- `reservationId` (reservationId) *(required)*: A unique identifier for the reservation, consistent in all markup.
- `reservationStatus` (reservationStatus) *(required)*: The reservation’s current status.
- `underName` (Person) *(required)*: The person renting the car.
- `provider` (Organization): The rental car agency.
- `broker` (Organization): An intermediary booking service.
- `url` (URL): A webpage the user can access to view reservation details.

## See Also

- [object FlightReservation](flightreservation.md)
  An airplane flight reservation.
- [object TrainReservation](trainreservation.md)
  A reservation for train travel.
- [object BusReservation](busreservation.md)
  A reservation for bus travel.
- [object BoatReservation](boatreservation.md)
  A reservation for boat travel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/rentalcarreservation)*