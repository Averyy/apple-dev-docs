# INAirport

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes an airport.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INAirport
```

```objc
@interface INAirport : NSObject
```

## Topics

### Initializing an Airport Object
- [init(name: String?, iataCode: String?, icaoCode: String?)](./inairport/init%28name,iatacode,icaocode%29.md)
  Creates a new airport object with the specified contents and attributes.
### Describing the Airport
- [var name: String?](./inairport/name.md)
  The name of the airport.
- [var iataCode: String?](./inairport/iatacode.md)
  The three-letter International Air Transport Association (IATA) code for the airport.
- [var icaoCode: String?](./inairport/icaocode.md)
  The four-letter International Civil Aviation Organization (ICAO) code for the airport.
### Initializers
- [init?(coder: NSCoder)](./inairport/init%28coder%29.md)

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
- [class INAirportGate](./inairportgate.md)
  The information that describes an arrival or departure gate for a flight.
- [var reservedSeat: INSeat?](./inflightreservation/reservedseat.md)
  The user’s seat for the flight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairport)*