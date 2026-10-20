# BusStation

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary  
**Role**: Object

The name and location of a bus station.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```
object BusStation
```

## Properties

- `@type` (string) *(required)*: **Allowed Values**: `BusStation`
- `address` (PostalAddress) *(required)*: The location of the bus station.
- `name` (string) *(required)*: The name of the bus station.

## See Also

### Defining a Bus Reservation
- [object BusTrip](./bustrip.md)
  Location and scheduling information for a bus trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/busstation)*