# reservedSeat

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The seat reserved for the user.

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

### Getting the Train Reservation Information
- [var trainTrip: INTrainTrip](./traintrip.md)
  An object containing the detailed information about the train trip.
- [class INTrainTrip](../intraintrip.md)
  The information that describes a train trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intrainreservation/reservedseat)*