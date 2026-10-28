# partySize

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The number of people in the guest’s party.

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

Use this information to identify time slots available at the restaurant. For large parties, restaurants may have a more limited number of time slots available.

## See Also

### Getting the Reservation Details
- [var preferredBookingDateComponents: DateComponents?](./preferredbookingdatecomponents.md)
  The date and time preferred by the user for the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent/partysize)*