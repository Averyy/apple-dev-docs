# reservedSeat

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s seat for the flight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var reservedSeat: INSeat? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSeat * reservedSeat;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSeat * reservedSeat;
```

## See Also

### Getting the Flight Reservation Information
- [var flight: INFlight](./flight.md)
  The flight information associated with the reservation.
- [class INFlight](../inflight.md)
  The information that describes a flight.
- [class INAirline](../inairline.md)
  The information that describes an airline.
- [class INAirport](../inairport.md)
  The information that describes an airport.
- [class INAirportGate](../inairportgate.md)
  The information that describes an arrival or departure gate for a flight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflightreservation/reservedseat)*