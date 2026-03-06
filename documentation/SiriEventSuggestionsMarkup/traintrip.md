# TrainTrip

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

Location and scheduling information for a train trip.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object TrainTrip
```

## Properties

- `@type` (string) *(required)*
- `arrivalStation` (TrainStation) *(required)*: The station where the train reservation ends.
- `arrivalTime` (dateTimeISO8601) *(required)*: The scheduled time the train arrives.
- `departureStation` (TrainStation) *(required)*: The station where the train reservation starts.
- `departureTime` (dateTimeISO8601) *(required)*: The scheduled time the train departs.
- `trainName` (string) *(required)*: The name of the train.
- `trainNumber` (string) *(required)*: The train’s route number or other identifier.
- `provider` (Organization): The railway providing the train trip.
- `arrivalPlatform` (string)
- `departurePlatform` (string)

## See Also

- [object TrainStation](trainstation.md)
  The name and location of a train station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/traintrip)*