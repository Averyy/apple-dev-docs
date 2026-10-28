# airline

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The airline on which the user is flying.

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
var airline: INAirline { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INAirline * airline;
```

*macOS*

```objc
@property (atomic, copy, readonly) INAirline * airline;
```

## Discussion

This property contains information specific to the airline associated with the reservation.

## See Also

### Getting the Flight Information
- [var flightNumber: String](./flightnumber.md)
  The number of a flight.
- [var boardingTime: INDateComponentsRange?](./boardingtime.md)
  The date and time during which the flight is boarding.
- [var flightDuration: INDateComponentsRange](./flightduration.md)
  The date and time range for the departure and arrival of the flight.
- [var departureAirportGate: INAirportGate](./departureairportgate.md)
  The gate from which the flight departs.
- [var arrivalAirportGate: INAirportGate](./arrivalairportgate.md)
  The gate at which the flight arrives


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflight/airline)*