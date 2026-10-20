# Airline

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary  
**Role**: Object

An airline’s name and identifier.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```
object Airline
```

## Properties

- `@type` (string) *(required)*: **Allowed Values**: `Airline`
- `iataCode` (string) *(required)*: The three-letter identifier of the airline.

  **Allowed Values**: `/^[A-Z]{3}$/`
- `name` (string) *(required)*: The name of the airline.

## See Also

### Defining a Flight Reservation
- [object Flight](./flight.md)
  Location and scheduling information for an airplane flight.
- [object Airport](./airport.md)
  The name and location of an airport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/airline)*