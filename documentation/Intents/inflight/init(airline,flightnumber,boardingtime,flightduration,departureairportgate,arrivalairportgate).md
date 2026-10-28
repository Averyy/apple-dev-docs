# init(airline:flightNumber:boardingTime:flightDuration:departureAirportGate:arrivalAirportGate:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new object containing information about a flight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(airline: INAirline, flightNumber: String, boardingTime: INDateComponentsRange?, flightDuration: INDateComponentsRange, departureAirportGate: INAirportGate, arrivalAirportGate: INAirportGate)
```

```objc
- (instancetype) initWithAirline:(INAirline *) airline flightNumber:(NSString *) flightNumber boardingTime:(INDateComponentsRange *) boardingTime flightDuration:(INDateComponentsRange *) flightDuration departureAirportGate:(INAirportGate *) departureAirportGate arrivalAirportGate:(INAirportGate *) arrivalAirportGate;
```

## Return Value

A new [`INFlight`](../inflight.md) object or `nil` if one can’t be created.

## Parameters

- `airline`: The airline on which the user is flying.
- `flightNumber`: The number of the flight. Flight numbers are specific to each airline.
- `boardingTime`: The date and time during which the flight boards.
- `flightDuration`: The date and time range for the departure and arrival times for the flight.
- `departureAirportGate`: The gate from which the flight departs.
- `arrivalAirportGate`: The gate at which the flight arrives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inflight/init(airline:flightnumber:boardingtime:flightduration:departureairportgate:arrivalairportgate:))*