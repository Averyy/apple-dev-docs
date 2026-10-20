# Ticket

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary  
**Role**: Object

Details about a ticket for transportation or an event.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```
object Ticket
```

## Properties

- `@type` (string) *(required)*: **Allowed Values**: `Ticket`
- `ticketedSeat` (Seat): The seat reserved for the passenger or attendee.
- `ticketNumber` (string): An identifier for the ticket.

## See Also

### Common Reservation Data
- [object Person](./person.md)
  A passenger, diner, lodging guest, or event attendee.
- [object Seat](./seat.md)
  The specific location reserved for the passenger.
- [object Organization](./organization.md)
  A business, transportation provider, or event organizer.
- [object Place](./place.md)
  A business, transportation hub, or event venue.
- [object PostalAddress](./postaladdress.md)
  A specific geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/ticket)*