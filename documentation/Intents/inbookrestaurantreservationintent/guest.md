# guest

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The identity of the guest associated with the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var guest: INRestaurantGuest? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurantGuest * guest;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurantGuest * guest;
```

#### Discussion

You can use this information to identify the user. After a reservation is successfully created, you can forward the user’s contact information to the restaurant so that it can communicate with the user directly.

## See Also

### Getting the Booking Details
- [var bookingDateComponents: DateComponents](./bookingdatecomponents.md)
  The date and time of the reservation.
- [var bookingIdentifier: String?](./bookingidentifier.md)
  The unique identifier associated with the initial reservation data.
- [var partySize: Int](./partysize.md)
  The total number of people in the user’s party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/guest)*