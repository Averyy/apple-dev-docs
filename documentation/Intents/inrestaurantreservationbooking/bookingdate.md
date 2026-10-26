# bookingDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time of the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var bookingDate: Date { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSDate * bookingDate;
```

*macOS*

```objc
@property (atomic, copy) NSDate * bookingDate;
```

## See Also

### Accessing the Booking Information
- [var bookingIdentifier: String](./bookingidentifier.md)
  The unique identifier associated with this reservation.
- [var isBookingAvailable: Bool](./isbookingavailable.md)
  A Boolean value indicating whether the time slot is available for booking.
- [var bookingDescription: String?](./bookingdescription.md)
  An optional description of the booking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/bookingdate)*