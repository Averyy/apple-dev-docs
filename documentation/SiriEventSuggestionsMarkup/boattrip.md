# BoatTrip

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

Location and scheduling information for a boat trip.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object BoatTrip
```

## Properties

- `@type` (string) *(required)*
- `arrivalBoatTerminal` (BoatTerminal) *(required)*: The terminal where the boat reservation ends.
- `arrivalTime` (dateTimeISO8601) *(required)*: The scheduled time the boat arrives.
- `departureBoatTerminal` (BoatTerminal) *(required)*: The terminal where the boat reservation begins.
- `departureTime` (dateTimeISO8601) *(required)*: The scheduled time the boat departs.
- `identifier` (string) *(required)*: The boat’s number or other identifier.
- `name` (string) *(required)*: The boat or boat route’s name.
- `provider` (Organization): The organization providing the boat trip.

## See Also

- [object BoatTerminal](boatterminal.md)
  The name and location of a boat terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/boattrip)*