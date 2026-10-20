# Person

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary  
**Role**: Object

A passenger, diner, lodging guest, or event attendee.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```
object Person
```

## Properties

- `@type` (string) *(required)*: **Allowed Values**: `Person`
- `name` (string) *(required)*: The participant, or a primary participant of a multiperson reservation if the reservation provider doesn’t require a name for each participant.

## See Also

### Common Reservation Data
- [object Ticket](./ticket.md)
  Details about a ticket for transportation or an event.
- [object Seat](./seat.md)
  The specific location reserved for the passenger.
- [object Organization](./organization.md)
  A business, transportation provider, or event organizer.
- [object Place](./place.md)
  A business, transportation hub, or event venue.
- [object PostalAddress](./postaladdress.md)
  A specific geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/person)*