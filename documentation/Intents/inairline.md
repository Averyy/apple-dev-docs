# INAirline

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes an airline.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INAirline
```

```objc
@interface INAirline : NSObject
```

## Topics

### Initializing an Airline Object
- [init(name: String?, iataCode: String?, icaoCode: String?)](./inairline/init%28name,iatacode,icaocode%29.md)
  Creates a new airline object with the specified contents and attributes.
### Describing the Airline
- [var name: String?](./inairline/name.md)
  The name of the airline.
- [var iataCode: String?](./inairline/iatacode.md)
  The two-letter International Air Transport Association (IATA) code for the airline.
- [var icaoCode: String?](./inairline/icaocode.md)
  The three-letter International Civil Aviation Organization (ICAO) code for the airline.
### Initializers
- [init?(coder: NSCoder)](./inairline/init%28coder%29.md)

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
- [class INAirport](./inairport.md)
  The information that describes an airport.
- [class INAirportGate](./inairportgate.md)
  The information that describes an arrival or departure gate for a flight.
- [var reservedSeat: INSeat?](./inflightreservation/reservedseat.md)
  The user’s seat for the flight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairline)*