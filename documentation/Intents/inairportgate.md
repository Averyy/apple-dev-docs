# INAirportGate

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes an arrival or departure gate for a flight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INAirportGate
```

```objc
@interface INAirportGate : NSObject
```

## Overview

This class contains all of the relevant information for a flight’s arrival or departure gate. Ensure that an instance of the object contains as much information as available. At a minimum, always include the airport for the flight.

## Topics

### Creating an Airport Gate
- [init(airport: INAirport, terminal: String?, gate: String?)](./inairportgate/init%28airport,terminal,gate%29.md)
  Creates a new gate object for a flight.
### Getting the Gate Information
- [var airport: INAirport](./inairportgate/airport.md)
  The airport from which a flight departs or arrives.
- [var terminal: String?](./inairportgate/terminal.md)
  The terminal from which a flight departs or arrives.
- [var gate: String?](./inairportgate/gate.md)
  An identifier for the gate.
### Initializers
- [init?(coder: NSCoder)](./inairportgate/init%28coder%29.md)

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
- [class INFlight](./inflight.md)
  The information that describes a flight.
- [class INAirline](./inairline.md)
  The information that describes an airline.
- [class INAirport](./inairport.md)
  The information that describes an airport.
- [var reservedSeat: INSeat?](./inflightreservation/reservedseat.md)
  The user’s seat for the flight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairportgate)*