# partySize

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The total number of people in the user’s party.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var partySize: Int { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) NSUInteger partySize;
```

*macOS*

```objc
@property (atomic) NSUInteger partySize;
```

## Discussion

The party size includes the person who initiated the reservation and all additional party members.

## See Also

### Getting the Booking Details
- [var bookingDateComponents: DateComponents](./bookingdatecomponents.md)
  The date and time of the reservation.
- [var bookingIdentifier: String?](./bookingidentifier.md)
  The unique identifier associated with the initial reservation data.
- [var guest: INRestaurantGuest?](./guest.md)
  The identity of the guest associated with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/partysize)*