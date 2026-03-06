# LodgingReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A hotel reservation or other booking for a place to stay.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object LodgingReservation
```

## Topics

### Defining a Lodging Reservation
- [object LodgingBusiness](lodgingbusiness.md)
  A hotel, inn, or other lodging location.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `checkinTime` (dateTimeISO8601) *(required)*: The earliest the guest may check in.
- `checkoutTime` (dateTimeISO8601) *(required)*: The latest the guest may check out.
- `reservationFor` (LodgingBusiness) *(required)*: The location of the lodging, such as a hotel or inn.
- `reservationId` (reservationId) *(required)*: A unique identifier for the reservation, consistent in all markup.
- `reservationStatus` (reservationStatus) *(required)*: The reservation’s current status.
- `underName` (Person) *(required)*: The lodging guest, or a primary guest if the event provider doesn’t require a name for each guest.
- `broker` (Organization): An intermediary booking service.
- `url` (URL): A webpage the user can access to view reservation details.

## See Also

- [object EventReservation](eventreservation.md)
  A reservation for a movie, sporting event, live show, or other scheduled event.
- [object FoodEstablishmentReservation](foodestablishmentreservation.md)
  A restaurant reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/lodgingreservation)*