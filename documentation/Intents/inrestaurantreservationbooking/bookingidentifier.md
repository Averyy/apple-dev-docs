# bookingIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier associated with this reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var bookingIdentifier: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * bookingIdentifier;
```

*macOS*

```objc
@property (atomic, copy) NSString * bookingIdentifier;
```

#### Discussion

Assign a unique identifier to this property that you can use later to complete the reservation. The identifier should be a string that you can use to look up the reservation details in your system.

## See Also

### Accessing the Booking Information
- [var isBookingAvailable: Bool](./isbookingavailable.md)
  A Boolean value indicating whether the time slot is available for booking.
- [var bookingDate: Date](./bookingdate.md)
  The date and time of the reservation.
- [var bookingDescription: String?](./bookingdescription.md)
  An optional description of the booking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/bookingidentifier)*