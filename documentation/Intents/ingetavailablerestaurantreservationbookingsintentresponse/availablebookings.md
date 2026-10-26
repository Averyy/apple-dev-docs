# availableBookings

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of available time slots for the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var availableBookings: [INRestaurantReservationBooking] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSArray<INRestaurantReservationBooking *> * availableBookings;
```

*macOS*

```objc
@property (atomic, readonly) NSArray<INRestaurantReservationBooking *> * availableBookings;
```

#### Discussion

This property contains the details of the reservation time slots that you are offering to the user. Offering a time slot does not by itself complete the booking process. The user must choose a time slot, at which time the system sends your Intents extension a [`INBookRestaurantReservationIntent`](../inbookrestaurantreservationintent.md) object, which you use to complete the booking process.

The value of this property is set automatically at initialization time and can’t be changed later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse/availablebookings)*