# guestProvidedSpecialRequestText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Any special requests made by the user with the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var guestProvidedSpecialRequestText: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * guestProvidedSpecialRequestText;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * guestProvidedSpecialRequestText;
```

## Discussion

Users can include special requests when booking a reservation. For example, the user might use request a non-smoking table or enumerate any dietary restrictions. If the user provides additional requests, this field contains that information.

## See Also

### Accessing the Reservation Information
- [var guest: INRestaurantGuest](./guest.md)
  The guest associated with the reservation.
- [var status: INRestaurantReservationUserBookingStatus](./status.md)
  The current status of the reservation.
- [var dateStatusModified: Date](./datestatusmodified.md)
  The date on which the status of the reservation changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/guestprovidedspecialrequesttext)*