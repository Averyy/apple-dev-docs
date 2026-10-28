# bookingDateComponents

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time of the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var bookingDateComponents: DateComponents { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSDateComponents * bookingDateComponents;
```

*macOS*

```objc
@property (atomic, copy) NSDateComponents * bookingDateComponents;
```

## Discussion

This date and time represent the values selected by the user.

## See Also

### Getting the Booking Details
- [var bookingIdentifier: String?](./bookingidentifier.md)
  The unique identifier associated with the initial reservation data.
- [var partySize: Int](./partysize.md)
  The total number of people in the user’s party.
- [var guest: INRestaurantGuest?](./guest.md)
  The identity of the guest associated with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/bookingdatecomponents)*