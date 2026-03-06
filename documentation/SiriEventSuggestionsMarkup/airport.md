# Airport

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

The name and location of an airport.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object Airport
```

## Properties

- `@type` (string) *(required)*
- `iataCode` (string) *(required)*: The airport’s official three-letter identifier.
- `name` (string): The name of the airport.
- `address` (PostalAddress): The location of the airport.

## See Also

- [object Flight](flight.md)
  Location and scheduling information for an airplane flight.
- [object Airline](airline.md)
  An airline’s name and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/airport)*