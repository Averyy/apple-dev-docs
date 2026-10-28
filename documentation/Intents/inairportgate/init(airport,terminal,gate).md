# init(airport:terminal:gate:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new gate object for a flight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(airport: INAirport, terminal: String?, gate: String?)
```

```objc
- (instancetype) initWithAirport:(INAirport *) airport terminal:(NSString *) terminal gate:(NSString *) gate;
```

## Return Value

A new [`INAirportGate`](../inairportgate.md) object or `nil` if one can’t be created.

## Discussion

You must create a new [`INAirportGate`](../inairportgate.md) object for both the arrival and departure gates associated with a flight.

## Parameters

- `airport`: The airport from which a flight departs or arrives.
- `terminal`: The terminal from which a flight departs or arrives.
- `gate`: The gate identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairportgate/init(airport:terminal:gate:))*