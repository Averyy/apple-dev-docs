# Organization

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary  
**Role**: Object

A business, transportation provider, or event organizer.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```
object Organization
```

## Properties

- `@type` (string) *(required)*: **Allowed Values**: `Organization`
- `name` (string) *(required)*: The name of the organization.

## See Also

### Common Reservation Data
- [object Person](./person.md)
  A passenger, diner, lodging guest, or event attendee.
- [object Ticket](./ticket.md)
  Details about a ticket for transportation or an event.
- [object Seat](./seat.md)
  The specific location reserved for the passenger.
- [object Place](./place.md)
  A business, transportation hub, or event venue.
- [object PostalAddress](./postaladdress.md)
  A specific geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/organization)*