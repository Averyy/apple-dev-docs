# bookingDescription

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An optional description of the booking.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var bookingDescription: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * bookingDescription;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * bookingDescription;
```

## Discussion

Use this property to provide a user-readable description of the reservation. For example, you might use this property to summarize the restaurant, date, and party information.

## See Also

### Accessing the Booking Information
- [var bookingIdentifier: String](./bookingidentifier.md)
  The unique identifier associated with this reservation.
- [var isBookingAvailable: Bool](./isbookingavailable.md)
  A Boolean value indicating whether the time slot is available for booking.
- [var bookingDate: Date](./bookingdate.md)
  The date and time of the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/bookingdescription)*