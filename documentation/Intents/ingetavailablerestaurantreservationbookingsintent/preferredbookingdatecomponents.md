# preferredBookingDateComponents

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time preferred by the user for the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var preferredBookingDateComponents: DateComponents? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSDateComponents * preferredBookingDateComponents;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSDateComponents * preferredBookingDateComponents;
```

#### Discussion

Use the value in this property as a guide for determining the list of time slots for reservations. If no reservations are available at the specified date, you may choose a different date, as long as it falls between the dates specified by the [`earliestBookingDateForResults`](./earliestbookingdateforresults.md) and [`latestBookingDateForResults`](./latestbookingdateforresults.md) properties.

## See Also

### Getting the Reservation Details
- [var partySize: Int](./partysize.md)
  The number of people in the guest’s party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent/preferredbookingdatecomponents)*