# boatTrip

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Information describing a voyage.

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
var boatTrip: INBoatTrip? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INBoatTrip * boatTrip;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INBoatTrip * boatTrip;
```

## See Also

### Getting the Boat Reservation Information
- [class INBoatTrip](../inboattrip.md)
  The information that describes a boat trip.
- [var reservedSeat: INSeat?](./reservedseat.md)
  The passenger’s seat on a boat reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboatreservation/boattrip)*