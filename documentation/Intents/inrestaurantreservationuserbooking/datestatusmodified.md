# dateStatusModified

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date on which the status of the reservation changed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var dateStatusModified: Date { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSDate * dateStatusModified;
```

*macOS*

```objc
@property (atomic, copy) NSDate * dateStatusModified;
```

## Discussion

When you change the [`status`](./status.md) property of the reservation, update this property with the date on which the status changed.

## See Also

### Accessing the Reservation Information
- [var guest: INRestaurantGuest](./guest.md)
  The guest associated with the reservation.
- [var status: INRestaurantReservationUserBookingStatus](./status.md)
  The current status of the reservation.
- [var guestProvidedSpecialRequestText: String?](./guestprovidedspecialrequesttext.md)
  Any special requests made by the user with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/datestatusmodified)*