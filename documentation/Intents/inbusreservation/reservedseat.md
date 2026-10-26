# reservedSeat

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Seat information for the bus reservation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

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

### Getting the Bus Trip Reservation Information
- [var busTrip: INBusTrip](./bustrip.md)
  Information describing a bus trip.
- [class INBusTrip](../inbustrip.md)
  Information describing a bus trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbusreservation/reservedseat)*