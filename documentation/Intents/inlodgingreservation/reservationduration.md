# reservationDuration

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time range that indicates the beginning and end of the reservation.

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
var reservationDuration: INDateComponentsRange { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INDateComponentsRange * reservationDuration;
```

*macOS*

```objc
@property (atomic, copy, readonly) INDateComponentsRange * reservationDuration;
```

#### Discussion

The beginning and end times for the reservation indicate the earliest time the user can check in and the latest time they can check out.

## See Also

### Getting the Lodging Reservation Information
- [var lodgingBusinessLocation: CLPlacemark](./lodgingbusinesslocation.md)
  The name and location of the lodging establishment.
- [var numberOfAdults: Int?](./numberofadults-6fsnq.md)
  The number of adults staying at the lodging location.
- [var numberOfChildren: Int?](./numberofchildren-1dm3g.md)
  The number of children staying at the lodging location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation/reservationduration)*