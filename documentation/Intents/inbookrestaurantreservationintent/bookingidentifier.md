# bookingIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier associated with the initial reservation data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var bookingIdentifier: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * bookingIdentifier;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * bookingIdentifier;
```

## Discussion

Prior to booking, your Intents extension provides a set of potential reservation options in the form of [`INRestaurantReservationBooking`](../inrestaurantreservationbooking.md) objects, each of which contains a unique booking identifier. When the user selects a reservation time, this property receives the booking identifier from the corresponding [`INRestaurantReservationBooking`](../inrestaurantreservationbooking.md) object. Use that value to get the details about the reservation option chosen by the user.

## See Also

### Getting the Booking Details
- [var bookingDateComponents: DateComponents](./bookingdatecomponents.md)
  The date and time of the reservation.
- [var partySize: Int](./partysize.md)
  The total number of people in the user’s party.
- [var guest: INRestaurantGuest?](./guest.md)
  The identity of the guest associated with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/bookingidentifier)*