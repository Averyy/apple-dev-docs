# Seat

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

The specific location reserved for the passenger.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object Seat
```

## Properties

- `@type` (string)
- `seatingType` (string): The reserved class of service.
- `seatNumber` (string): The identifier for a particular seat in a row of seats.
- `seatRow` (string): The identifier for a particular row in a section of seats.
- `seatSection` (string): The identifier for a particular group of seats.

## See Also

- [object Person](person.md)
  A passenger, diner, lodging guest, or event attendee.
- [object Ticket](ticket.md)
  Details about a ticket for transportation or an event.
- [object Organization](organization.md)
  A business, transportation provider, or event organizer.
- [object Place](place.md)
  A business, transportation hub, or event venue.
- [object PostalAddress](postaladdress.md)
  A specific geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/seat)*