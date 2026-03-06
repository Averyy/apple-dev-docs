# Flight

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

Location and scheduling information for an airplane flight.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object Flight
```

## Properties

- `@type` (string) *(required)*
- `arrivalAirport` (Airport) *(required)*: The airport where the flight ends.
- `arrivalGate` (string): The airport gate where the flight ends.
- `arrivalTerminal` (string): The airport terminal where the flight ends.
- `arrivalTime` (dateTimeISO8601) *(required)*: The scheduled date and time, in the airport’s local time zone, that the flight ends.
- `departureAirport` (Airport) *(required)*: The airport where the flight begins.
- `departureGate` (string): The airport gate where the flight begins.
- `departureTerminal` (string): The airport terminal where the flight begins.
- `departureTime` (dateTimeISO8601) *(required)*: The scheduled date and time, in the airport’s local time zone, that the flight begins.
- `flightNumber` (string) *(required)*: The flight number, specific to an airline.
- `provider` (Airline) *(required)*: The airline providing the flight.

## See Also

- [object Airline](airline.md)
  An airline’s name and identifier.
- [object Airport](airport.md)
  The name and location of an airport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/flight)*