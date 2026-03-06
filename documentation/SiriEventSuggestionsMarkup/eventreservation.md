# EventReservation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A reservation for a movie, sporting event, live show, or other scheduled event.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object EventReservation
```

## Topics

### Defining an Event Reservation
- [object Event](event.md)
  A sporting event, live show, or other scheduled event.

## Properties

- `@context` (@context) *(required)*
- `@type` (string) *(required)*
- `reservationFor` (Event) *(required)*: General information about the event.
- `reservationId` (reservationId) *(required)*: A unique identifier for the reservation, consistent in all markup.
- `reservationStatus` (reservationStatus) *(required)*: The reservation’s current status.
- `reservedTicket` (Ticket): Details about the attendee’s ticketed seat.
- `underName` (Person) *(required)*: The event attendee, or a primary attendee if the event provider doesn’t require a name for each attendee.
- `broker` (Organization): An intermediary booking service.
- `url` (URL): A webpage the user can access to view reservation details.

## See Also

- [object FoodEstablishmentReservation](foodestablishmentreservation.md)
  A restaurant reservation.
- [object LodgingReservation](lodgingreservation.md)
  A hotel reservation or other booking for a place to stay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/eventreservation)*