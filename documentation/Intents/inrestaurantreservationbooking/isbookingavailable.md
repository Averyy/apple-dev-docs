# isBookingAvailable

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the time slot is available for booking.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isBookingAvailable: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, getter=isBookingAvailable) BOOL bookingAvailable;
```

*macOS*

```objc
@property (atomic, getter=isBookingAvailable) BOOL bookingAvailable;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md). Change it to [`false`](../../Swift/false.md) if the specified time slot is unavailable, either because the restaurant is fully booked at that time or because it cannot accommodate a party of the specified size at that time.

## See Also

### Accessing the Booking Information
- [var bookingIdentifier: String](./bookingidentifier.md)
  The unique identifier associated with this reservation.
- [var bookingDate: Date](./bookingdate.md)
  The date and time of the reservation.
- [var bookingDescription: String?](./bookingdescription.md)
  An optional description of the booking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/isbookingavailable)*