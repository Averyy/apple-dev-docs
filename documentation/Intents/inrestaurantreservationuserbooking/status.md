# status

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current status of the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var status: INRestaurantReservationUserBookingStatus { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) INRestaurantReservationUserBookingStatus status;
```

*macOS*

```objc
@property (atomic) INRestaurantReservationUserBookingStatus status;
```

## Discussion

Upon receipt of a reservation, your Intents extension works with the restaurant to place the reservation. This property contains the status of whether the restaurant accepted or declined the reservation, or whether the reservation is still pending while you communicate the details of the reservation to the restaurant.

When the value of this property changes, update the [`dateStatusModified`](./datestatusmodified.md) property as well.

## See Also

### Accessing the Reservation Information
- [var guest: INRestaurantGuest](./guest.md)
  The guest associated with the reservation.
- [var dateStatusModified: Date](./datestatusmodified.md)
  The date on which the status of the reservation changed.
- [var guestProvidedSpecialRequestText: String?](./guestprovidedspecialrequesttext.md)
  Any special requests made by the user with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/status)*