# BusTrip

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

Location and scheduling information for a bus trip.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object BusTrip
```

## Properties

- `@type` (string) *(required)*
- `arrivalBusStop` (BusStation) *(required)*: The station where the bus reservation ends.
- `arrivalTime` (dateTimeISO8601) *(required)*: The scheduled time the bus arrives.
- `busName` (string) *(required)*: The name of the bus.
- `busNumber` (string) *(required)*: The bus’s route number or other identifier.
- `departureBusStop` (BusStation) *(required)*: The station where the bus reservation starts.
- `departureTime` (dateTimeISO8601) *(required)*: The scheduled time the bus departs.
- `provider` (Organization): The bus company.

## See Also

- [object BusStation](busstation.md)
  The name and location of a bus station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/bustrip)*