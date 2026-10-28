# guest

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The guest associated with the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var guest: INRestaurantGuest { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) INRestaurantGuest * guest;
```

*macOS*

```objc
@property (atomic, copy) INRestaurantGuest * guest;
```

## Discussion

Normally, the guest is the same person who made the reservation. However, If your app lets users edit the name on a reservation, the guest may be different.

## See Also

### Accessing the Reservation Information
- [var status: INRestaurantReservationUserBookingStatus](./status.md)
  The current status of the reservation.
- [var dateStatusModified: Date](./datestatusmodified.md)
  The date on which the status of the reservation changed.
- [var guestProvidedSpecialRequestText: String?](./guestprovidedspecialrequesttext.md)
  Any special requests made by the user with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/guest)*