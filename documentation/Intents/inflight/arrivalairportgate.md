# arrivalAirportGate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The gate at which the flight arrives

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
var arrivalAirportGate: INAirportGate { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INAirportGate * arrivalAirportGate;
```

*macOS*

```objc
@property (atomic, copy, readonly) INAirportGate * arrivalAirportGate;
```

#### Discussion

The [`INAirportGate`](../inairportgate.md) object contains information about the airport, gate, and terminal for the flight’s arrival.

## See Also

### Getting the Flight Information
- [var airline: INAirline](./airline.md)
  The airline on which the user is flying.
- [var flightNumber: String](./flightnumber.md)
  The number of a flight.
- [var boardingTime: INDateComponentsRange?](./boardingtime.md)
  The date and time during which the flight is boarding.
- [var flightDuration: INDateComponentsRange](./flightduration.md)
  The date and time range for the departure and arrival of the flight.
- [var departureAirportGate: INAirportGate](./departureairportgate.md)
  The gate from which the flight departs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflight/arrivalairportgate)*