# flightNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The number of a flight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var flightNumber: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * flightNumber;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * flightNumber;
```

## Discussion

This property doesn’t include the IATA or ICAO code of the airline associated with the flight.

## See Also

### Getting the Flight Information
- [var airline: INAirline](./airline.md)
  The airline on which the user is flying.
- [var boardingTime: INDateComponentsRange?](./boardingtime.md)
  The date and time during which the flight is boarding.
- [var flightDuration: INDateComponentsRange](./flightduration.md)
  The date and time range for the departure and arrival of the flight.
- [var departureAirportGate: INAirportGate](./departureairportgate.md)
  The gate from which the flight departs.
- [var arrivalAirportGate: INAirportGate](./arrivalairportgate.md)
  The gate at which the flight arrives


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflight/flightnumber)*