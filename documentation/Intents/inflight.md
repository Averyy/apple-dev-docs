# INFlight

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a flight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INFlight
```

```objc
@interface INFlight : NSObject
```

## Topics

### Initializing a Flight Object
- [init(airline: INAirline, flightNumber: String, boardingTime: INDateComponentsRange?, flightDuration: INDateComponentsRange, departureAirportGate: INAirportGate, arrivalAirportGate: INAirportGate)](./inflight/init%28airline,flightnumber,boardingtime,flightduration,departureairportgate,arrivalairportgate%29.md)
  Creates a new object containing information about a flight.
### Getting the Flight Information
- [var airline: INAirline](./inflight/airline.md)
  The airline on which the user is flying.
- [var flightNumber: String](./inflight/flightnumber.md)
  The number of a flight.
- [var boardingTime: INDateComponentsRange?](./inflight/boardingtime.md)
  The date and time during which the flight is boarding.
- [var flightDuration: INDateComponentsRange](./inflight/flightduration.md)
  The date and time range for the departure and arrival of the flight.
- [var departureAirportGate: INAirportGate](./inflight/departureairportgate.md)
  The gate from which the flight departs.
- [var arrivalAirportGate: INAirportGate](./inflight/arrivalairportgate.md)
  The gate at which the flight arrives
### Initializers
- [init?(coder: NSCoder)](./inflight/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Getting the Flight Reservation Information
- [var flight: INFlight](./inflightreservation/flight.md)
  The flight information associated with the reservation.
- [class INAirline](./inairline.md)
  The information that describes an airline.
- [class INAirport](./inairport.md)
  The information that describes an airport.
- [class INAirportGate](./inairportgate.md)
  The information that describes an arrival or departure gate for a flight.
- [var reservedSeat: INSeat?](./inflightreservation/reservedseat.md)
  The user’s seat for the flight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflight)*