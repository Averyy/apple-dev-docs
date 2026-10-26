# flightDuration

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time range for the departure and arrival of the flight.

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
var flightDuration: INDateComponentsRange { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INDateComponentsRange * flightDuration;
```

*macOS*

```objc
@property (atomic, copy, readonly) INDateComponentsRange * flightDuration;
```

## See Also

### Getting the Flight Information
- [var airline: INAirline](./airline.md)
  The airline on which the user is flying.
- [var flightNumber: String](./flightnumber.md)
  The number of a flight.
- [var boardingTime: INDateComponentsRange?](./boardingtime.md)
  The date and time during which the flight is boarding.
- [var departureAirportGate: INAirportGate](./departureairportgate.md)
  The gate from which the flight departs.
- [var arrivalAirportGate: INAirportGate](./arrivalairportgate.md)
  The gate at which the flight arrives


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflight/flightduration)*